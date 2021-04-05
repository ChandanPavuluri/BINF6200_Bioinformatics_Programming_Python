"""
config.py
#config.py
"""
_UNIGENE_DIR = "C:/Users/ckpav/PycharmProjects/BINF6200/A5/data_directories"
_UNIGENE_FILE_ENDING = "unigene"


def get_unigene_directory():
    return _UNIGENE_DIR


def get_unigene_extension():
    return _UNIGENE_FILE_ENDING


def get_host_keywords():
    bos_tarus = "Bos_taurus"
    homo_sapiens = "Homo_sapiens"
    equus_caballus = "Equus_caballus"
    mus_musculus = "Mus_musculus"
    ovis_aries = "Ovis_aries"
    rattus_norvegicus = "Rattus_norvegicus"

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
    return host_keywords


def get_error_string_4_unable_to_open():
    print(f"Could not open the file (unable to open)")