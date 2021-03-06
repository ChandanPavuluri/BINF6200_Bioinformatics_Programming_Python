import pytest
import os
from pdb_fasta_splitter import get_fh, get_header_and_sequence_lists, file_write



FASTA_STRING = """\
>E123 sequence
ATGCTAGCTA
"""

TEST_FILE = open("fasta.txt","w")
TEST_FILE.write(FASTA_STRING)
TEST_FILE.close()


def test_get_fh_4_IOError():
    """ Test function for get_fh error"""
    # does it raise IOError
    # this should exit
    with pytest.raises(IOError):
        get_fh("does_not_exist.txt", "r")


def test_get_header_and_sequence_lists():
    fh_in = get_fh("fasta.txt", "r")
    assert get_header_and_sequence_lists(fh_in) == (['>E123 sequence'], ['ATGCTAGCTA'])

def test_file_write():
    fh_in = get_fh("fasta.txt", "r")
    list_headers, list_seqs = get_header_and_sequence_lists(fh_in)
    assert file_write(list_headers, list_seqs) == (1,0)
    os.remove("pdb_protein.fasta")
    os.remove("pdb_ss.fasta")
    os.remove("fasta.txt")



