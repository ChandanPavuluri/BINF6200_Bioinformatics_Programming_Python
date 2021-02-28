import pytest
from nucleotide_statistics_from_fasta import get_fh, get_header_and_sequence_lists, print_sequence_stats


def test_get_fh_4_IOError():
    # does it raise IOError
    # this should exit
    with pytest.raises(IOError):
        get_fh("does_not_exist.txt", "r")


def test_get_header_and_sequence_lists():
    fh_in = get_fh("test.txt", "r")
    assert get_header_and_sequence_lists(fh_in) == (['>1 sequence'], ['ATGCTAGCTA'])

def test_print_sequence_stats():
    fh_in = get_fh("test.txt", "r")
    list_headers, list_seqs = get_header_and_sequence_lists(fh_in)
    fh_out = get_fh("output.txt", "w")
    print_sequence_stats(list_headers, list_seqs, fh_out) == (["1", "1", "3", "2", "2", "3", "0", "10", "40.0"])
