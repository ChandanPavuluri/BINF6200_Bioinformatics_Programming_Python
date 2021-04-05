"""
gene_information_query.py
#gene_information_query.py
"""

# importing required modules
import argparse
import sys
import re
from assignment5 import my_io
from assignment5 import config


def main():
    args = args_parse()
    gene = args.GENE
    host,temp_host = modify_host_name(args.HOST)
    file = "/".join((config.get_unigene_directory(), host, gene + "." + config.get_unigene_extension()))
    print(file)
    if my_io.is_valid_gene_file_name(file):
        print(f"\nFound Gene {gene} for {temp_host}")
    else:
        print("Not found")
        print(f"Gene {gene} does not exist for {temp_host}. exiting now...", file=sys.stderr)
        sys.exit()
    tissues = get_gene_data(file)
    print_output(temp_host,gene,tissues)

def args_parse():
    """
    Function for command line arguments
    @return: Instance of argparse arguments
    """

    # Creating argument parser object
    parser = argparse.ArgumentParser(description='Give the Host and Gene name')

    # adding arguments that are needed
    parser.add_argument('-host', dest='HOST', help='Name of Host',
                        default="Human")
    parser.add_argument('-gene', dest='GENE', help='Name of Gene',
                        default="TGM1")

    return parser.parse_args()


def modify_host_name(host_name):
    dict = config.get_host_keywords()
    host_name = host_name.lower()
    host_name = re.sub("_"," ",host_name)

    if host_name not in dict.keys():
        _print_host_directories()
        sys.exit()
    else:
        host = dict[host_name]
        temp_host = re.sub("_"," ",host)
        return host,temp_host


def _print_host_directories():
    dict = config.get_host_keywords()
    scientific_name = set(dict.values())
    scientific_name = list(scientific_name)

    print("\nHere is a (non-case sensitive) list of available Hosts by scientific name")
    for (i, item) in enumerate(scientific_name, start=1):
        print(f"{i}. {item}")

    common_name = list(dict.keys())

    print("\nHere is a (non-case sensitive) list of available Hosts by common name")
    for (i, item) in enumerate(common_name, start=1):
        item = item.capitalize()
        print(f"{i}. {item}")

def get_gene_data(file_name):
    fh_in = my_io.get_fh(file_name, "r")
    for line in fh_in:
        if re.search("EXPRESS", line):
            line = line.replace("\n", "")
            line = re.sub('[A-Z]', "",line)
            line = line.split("|")
            line = [element.strip(' ') for element in line]
            line.sort()
            return line


def print_output(host,gene,tissue_list):
    count = len(tissue_list)
    print(f"In {host}, There are {count} tissues that {gene} is expressed in:\n")
    for (i, item) in enumerate(tissue_list, start=1):
        item = item.capitalize()
        print(f"{i}. {item}")


if __name__ == "__main__":
    main()