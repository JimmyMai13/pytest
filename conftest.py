import pytest
import os
import logging

log = logging.getLogger('TestUsers')

from .base import Base
from .pageobjects.base_page import BasePage

@pytest.fixture
def fix_base():
    base = Base()

    return base
