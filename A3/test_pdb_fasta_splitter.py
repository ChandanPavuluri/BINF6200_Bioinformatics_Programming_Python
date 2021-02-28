import pytest
from pdb_fasta_splitter import get_fh , get_header_and_sequence_lists,


def test_get_fh_4_IOError():
    # does it raise IOError
    # this should exit
    with pytest.raises(IOError):
        get_fh("does_not_exist.txt", "r")


def test_get_header_and_sequence_lists(input_file):
    fh_in = get_fh("test.txt", "r")
    assert_get_header_and_sequence_lists(fh_in) == [],[]