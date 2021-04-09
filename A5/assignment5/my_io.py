"""
my_io.py
Importing this for opening the files in programs
"""
import os


def get_fh(input_file, read_write):
    """
    Function for opening the file
    @param input_file: File 2 open
    @param read_write: method reading or writing
    @return return file_handle
    """
    # using try and except to catch the errors if its an IOError and ValueError
    try:
        file_to_open = open(input_file, read_write)
        return file_to_open
    except IOError:
        raise IOError from None
    except ValueError:
        raise ValueError

def is_valid_gene_file_name(file):
    """ checks if the gene exits """
    return os.path.exists(file)
