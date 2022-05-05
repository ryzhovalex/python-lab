from functools import wraps

import pytest


@pytest.fixture
def super_file_path():
    return "super_file.txt" 


@pytest.fixture
def apple():
    return "apple"


def file_ctx(func):
    @wraps(func)
    def test_wrapper(super_file_path, *args, **kwargs):
        with open(super_file_path, "r") as f:
            func(*args, **kwargs)
    return test_wrapper

