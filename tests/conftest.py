import pytest
import random

@pytest.fixture
def base_id():
    return random.randint(1,10000)