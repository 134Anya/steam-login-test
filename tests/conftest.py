import random
import time

import pytest
import requests
from faker import Faker

from logger.logger import Logger
from services.auth.auth_service import AuthService
from services.auth.models.login_request import LoginRequest
from services.auth.models.register_request import RegisterRequest
from services.university.models.enums import DegreeEnum, SubjectEnum
from services.university.models.group_request import GroupRequest
from services.university.models.student_request import StudentRequest
from services.university.models.teacher_request import TeacherRequest
from services.university.university_service import UniversityService
from utils.api_utils import ApiUtils

faker = Faker()


def wait_for_service(url, service_name, timeout=60):
    start_time = time.time()
    check_url = f"{url.rstrip('/')}/docs"
    while time.time() < start_time + timeout:
        try:
            response = requests.get(check_url, timeout=5)
            if response.status_code == 200:
                Logger.info(f"{service_name} is READY!")
                return
        except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError):
            time.sleep(1)
    raise RuntimeError(f"{service_name} did not start at {check_url}")


@pytest.fixture(scope="session", autouse=True)
def wait_for_auth_service():
    wait_for_service(AuthService.SERVICE_URL, "Auth API")


@pytest.fixture(scope="session", autouse=True)
def wait_for_university_service():
    wait_for_service(UniversityService.SERVICE_URL, "University API")


@pytest.fixture(scope="session", autouse=True)
def wait_for_auth_service():
    wait_for_service(AuthService.SERVICE_URL, "Auth API")


@pytest.fixture(scope="session", autouse=True)
def wait_for_university_service():
    wait_for_service(UniversityService.SERVICE_URL, "University API")


@pytest.fixture(scope="session")
def auth_api_utils_anonym():
    return ApiUtils(url=AuthService.SERVICE_URL)


@pytest.fixture(scope="session")
def access_token(auth_api_utils_anonym):
    auth_service = AuthService(auth_api_utils_anonym)
    username = faker.user_name()
    password = faker.password(length=20, special_chars=True, digits=True)

    auth_service.register_user(
        RegisterRequest(
            username=username,
            password=password,
            password_repeat=password,
            email=faker.email(),
        )
    )
    login_response = auth_service.login_user(
        LoginRequest(username=username, password=password)
    )
    return login_response.access_token


@pytest.fixture(scope="session")
def university_api_utils_admin(access_token):
    return ApiUtils(
        url=UniversityService.SERVICE_URL,
        headers={"Authorization": f"Bearer {access_token}"},
    )


@pytest.fixture(scope="function")
def temp_group(university_api_utils_admin):
    service = UniversityService(university_api_utils_admin)
    group = service.create_group(GroupRequest(name=faker.word()))
    yield group
    try:
        service.delete_group(group.id)
    except Exception as e:
        Logger.info(f"Group {group.id} already deleted")


@pytest.fixture(scope="function")
def temp_student(university_api_utils_admin, temp_group):
    service = UniversityService(university_api_utils_admin)
    payload = StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        degree=random.choice([o.value for o in DegreeEnum]),
        phone=faker.numerify("+7#########"),
        group_id=temp_group.id,
    )
    student = service.create_student(payload)
    yield student
    try:
        service.delete_student(student.id)
    except Exception as e:
        Logger.info(f"Student {student.id} already deleted")


@pytest.fixture(scope="function")
def temp_teacher(university_api_utils_admin):
    service = UniversityService(university_api_utils_admin)
    payload = TeacherRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        subject=random.choice([o.value for o in SubjectEnum]),
    )
    teacher = service.create_teacher(payload)
    yield teacher
    try:
        service.delete_teacher(teacher.id)
    except Exception:
        Logger.error(f"Cleanup failed for teacher {teacher.id}")
