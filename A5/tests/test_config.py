"""
Test Suite of config.py
"""

# Importing the required modules
import os
import pytest

# importing functions from program file to test the program
from assignment5 import config

# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore all "Function name "test_get_fh_4_IOError" doesn't conform to snake_case naming style"
# pylint: disable=C0103




_UNIGENE_DIR = "/data/PROGRAMMING/assignment5"
_UNIGENE_FILE_ENDING = "unigene"

def test_get_unigene_directory():
    # checks if it returns the absolute path to the program data
    assert os.path.exists(config.get_unigene_directory()) == True

def test_get_unigene_extension():
    # checks if it returns the file extension
    assert config.get_unigene_extension() == "unigene"

def test_get_host_keywords():
    # does it map common names with scientific names correctly
    host = config.get_host_keywords()
    assert host['cow'] == 'Bos_taurus'
    assert host['bos taurus'] == 'Bos_taurus'
    assert host['human'] == 'Homo_sapiens'
    assert host['homo sapiens'] == 'Homo_sapiens'
    assert host['equus caballus'] == 'Equus_caballus'
    assert host['mus musculus'] == 'Mus_musculus'
    assert host['ovis aries'] == 'Ovis_aries'
    assert host['rattus norvegicus'] == 'Rattus_norvegicus'