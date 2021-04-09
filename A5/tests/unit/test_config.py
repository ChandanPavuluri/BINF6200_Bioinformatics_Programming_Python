"""
Test Suite of config.py
"""

# Importing the required modules
import os
# import pytest

# importing functions from program file to test the program
from assignment5 import config

# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore all "Function name "test_get_fh_4_IOError" doesn't conform to snake_case naming style"
# pylint: disable=C0103


_UNIGENE_DIR = "/home/chandan/BINF6200/A5/data_directories"
_UNIGENE_FILE_ENDING = "unigene"


def test_get_unigene_directory():
    # checks if it returns the absolute path to the program data
    assert os.path.exists(config.get_unigene_directory()) is True


def test_get_unigene_extension():
    # checks if it returns the file extension
    assert config.get_unigene_extension() == "unigene"


def test_get_host_keywords():
    # does it map common names with scientific names correctly
    host_dict = config.get_host_keywords()
    assert host_dict['cow'] == 'Bos_taurus'
    assert host_dict['bos taurus'] == 'Bos_taurus'
    assert host_dict['human'] == 'Homo_sapiens'
    assert host_dict['homo sapiens'] == 'Homo_sapiens'
    assert host_dict['equus caballus'] == 'Equus_caballus'
    assert host_dict['mus musculus'] == 'Mus_musculus'
    assert host_dict['ovis aries'] == 'Ovis_aries'
    assert host_dict['rattus norvegicus'] == 'Rattus_norvegicus'


def test_get_error_string_4_ValueError():
    assert config.get_error_string_4_ValueError() == print("Invalid argument "
                                                           "Value for opening a file for reading/writing")


def test_get_error_string_4_TypeError():
    assert config.get_error_string_4_TypeError() == print("Invalid argument Type passed in:")
