import os
import pytest

# importing functions from program file to test the program
from assignment4 import my_io

# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore all "Function name "test_get_fh_4_IOError" doesn't conform to snake_case naming style"
# pylint: disable=C0103

FILE_2_TEST = "test.txt"

def _create_test_file(file):
    # not actually run, the are just helper functions for the test script
    # create a test file
    open(file, "w").close()

def test_existing_get_fh_4_reading():
   # does it open a file for reading
   # create a test file
    _create_test_file(FILE_2_TEST)
    # test
    test = my_io.get_fh(FILE_2_TEST, "r")
    assert hasattr(test, "readline") is True, "Not able to open for reading"
    test.close()
    os.remove(FILE_2_TEST)


def test_existing_get_fh_4_writing():
    # does it open a file for writing
    # test
    test = my_io.get_fh(FILE_2_TEST, "w")
    assert hasattr(test, "write") is True, "Not able to open for writing"
    test.close()
    os.remove(FILE_2_TEST)


def test_get_fh_4_IOError():
    # does it raise IOError
    # this should exit
    with pytest.raises(IOError):
        my_io.get_fh("does_not_exist.txt", "r")


def test_get_fh_4_ValueError():
    # does it raise ValueError
    # this should exit
    _create_test_file(FILE_2_TEST)
    with pytest.raises(ValueError):
        my_io.get_fh("does_not_exist.txt", "rrr")
        os.remove(FILE_2_TEST)
