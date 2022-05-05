# Not worked, decided to use another ways.
from conftest import file_ctx


@file_ctx
def test_file(apple):
    print(apple)
    print(f)
    assert apple == "apple"

def test_apple(apple):
    print(apple)
    assert apple == "apple"
