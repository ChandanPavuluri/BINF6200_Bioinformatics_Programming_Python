"""Test suite for nucleotide_statistics_from_fasta.py"""

# Importing the required modeules
import os
import pytest


# importing functions from program file to test the program
from nucleotide_statistics_from_fasta import get_fh, get_header_and_sequence_lists, \
    _get_accession, _get_nt_occurrence, print_sequence_stats

# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore all "function name "test_get_fh_IOError" doesn't conform to snake_case naming style
# pylint: disable=C0103

FILE_2_TEST = "test.txt"

FASTA_STRING = """\
>E123 sequence
ATGCTAGCTA
"""

TEST_FILE = open("fasta.txt", "w")
TEST_FILE.write(FASTA_STRING)
TEST_FILE.close()


def _create_test_file(file):
    # not actually run, helper function for test script
    # create a test file
    open(file, "w").close()


def test_existing_get_fh_4_reading():
    # does it open file for reading
    # create a test file
    _create_test_file(FILE_2_TEST)

    # test
    test = get_fh(FILE_2_TEST, "r")
    assert hasattr(test, "readline") is True, "Not able to open for reading"
    test.close()
    os.remove(FILE_2_TEST)


def test_get_fh_4_IOError():
    # does it raise IOError
    # this should exit
    with pytest.raises(IOError):
        get_fh("does_not_exist.txt", "r")


def test_get_header_and_sequence_lists():
    # does it return the lists
    fh_in = get_fh("fasta.txt", "r")
    assert get_header_and_sequence_lists(fh_in) == (['>E123 sequence'], ['ATGCTAGCTA'])


def test__get_accession__get_nt_occurrence():
    # does it correctly cuts the header to give accession number
    fh_in = get_fh("fasta.txt", "r")
    list_headers, list_seqs = get_header_and_sequence_lists(fh_in)
    assert _get_accession(list_headers[0]) == "E123"
    assert _get_nt_occurrence("A", list_seqs[0]) == 3


def test_print_sequence_stats():
    # does it correctly return the stats
    fh_in = get_fh("fasta.txt", "r")
    list_headers, list_seqs = get_header_and_sequence_lists(fh_in)
    fh_out = get_fh("output.txt", "w")
    assert print_sequence_stats(list_headers, list_seqs, fh_out) == \
           (["1", "E123", "3", "2", "2", "3", "0", "10", "40.0"])
    os.remove("output.txt")


os.remove("fasta.txt")
