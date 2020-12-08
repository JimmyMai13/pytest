import pytest
from .base import Base


@pytest.fixture
def fix_base():
    base = Base()

    return base
