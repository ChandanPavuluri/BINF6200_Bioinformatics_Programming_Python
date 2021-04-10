"""
my_io.py
Importing this for opening the files in programs
"""
import os
from assignment5 import config

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
        config.get_error_string_4_IOError(input_file, read_write)
        raise IOError
    except ValueError:
        config.get_error_string_4_ValueError()
        raise ValueError()


def is_valid_gene_file_name(file):
    """ checks if the gene exits """
    return os.path.exists(file)
