"""
config.py
#config.py
"""

# Error" doesn't conform to snake_case naming style
# pylint: disable=invalid-name

_UNIGENE_DIR = "C:/Users/ckpav/OneDrive/Desktop/A5/data_directories"
_UNIGENE_FILE_ENDING = "unigene"


def get_unigene_directory():
    """ return the Directory absolute path"""
    return _UNIGENE_DIR


def get_unigene_extension():
    """return the extension"""
    return _UNIGENE_FILE_ENDING


def get_host_keywords():
    """ return a dictionary of the hosts"""

    # assigning to the variable
    bos_tarus = "Bos_taurus"
    homo_sapiens = "Homo_sapiens"
    equus_caballus = "Equus_caballus"
    mus_musculus = "Mus_musculus"
    ovis_aries = "Ovis_aries"
    rattus_norvegicus = "Rattus_norvegicus"

    # creating a dictionary
    host_keywords = {
        "bos taurus": bos_tarus,
        "cow": bos_tarus,
        "cows": bos_tarus,
        "homo sapiens": homo_sapiens,
        "human": homo_sapiens,
        "humans": homo_sapiens,
        "equus caballus": equus_caballus,
        "horse": equus_caballus,
        "horses": equus_caballus,
        "mus musculus": mus_musculus,
        "mouse": mus_musculus,
        "mouses": mus_musculus,
        "ovis aries": ovis_aries,
        "sheep": ovis_aries,
        "sheeps": ovis_aries,
        "rattus norvegicus": rattus_norvegicus,
        "rat": rattus_norvegicus,
        "rats": rattus_norvegicus
    }

    # returns the dictionary
    return host_keywords


def get_error_string_4_ValueError():
    """ Print the invalid argument type message and exits the program """
    print("Invalid argument Value for opening a file for reading/writing")


def get_error_string_4_TypeError():
    """ Print the invalid argument type message and exits the program """
    print("Invalid argument Type passed in:")


def get_error_string_4_IOError(file=None, mode=None):
    """ Print the invalid argument type message and exits the program """
    print(f"Could not open the file: {file} for mode '{mode}'")
