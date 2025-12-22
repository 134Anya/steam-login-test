import pytest
from core.singleton import DriverSingleton

@pytest.fixture(scope="session")
def driver():
    driver_instance = DriverSingleton().get_driver()
    yield driver_instance
    DriverSingleton().close_driver()