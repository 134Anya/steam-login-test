import pytest


@pytest.fixture
def api_data():
    return "Нагрузочная фикстура"

@pytest.fixture
def load_limit():
    return 9999
