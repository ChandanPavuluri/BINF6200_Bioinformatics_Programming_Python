import argparse
import sys
import re
from assignment5 import my_io
from assignment5 import config

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
    if host_name not in dict.keys():
        _print_host_directories()
        sys.exit()
    else:
        host = dict[host_name]
        return host



def _print_host_directories():
    dict = config.get_host_keywords()
    scientific_name= set(dict.values())
    print("\nHere is a (non-case sensitive) list of available Hosts by scientific name")
    for (i, item) in enumerate(scientific_name, start=1):
        print(f"{i}. {item}")

    common_name = list(dict.keys())

    print("\nHere is a (non-case sensitive) list of available Hosts by common name")
    for (i, item) in enumerate(common_name, start=1):
        item = str(item)
        item = item.capitalize()
        print(f"{i}. {item}")

def get_gene_data(file_name):
    fh_in = my_io.get_fh(file_name, "r")
    for line in fh_in:
        if re.search("EXPRESS", line):
            line = line.replace("\n", "")
            print(line)
            line = re.sub('[A-Z]', "",line)
            print(line)
            line = line.split("|")
            line = [element.strip(' ') for element in line]
            print(line)
            for (i, item) in enumerate(line, start=1):
                print(f"{i}. {item}")




if __name__ == "__main__":
    args = args_parse()
    gene = args.GENE
    host = modify_host_name(args.HOST)
    file = "/".join((config.get_unigene_directory(), host, gene + "." + config.get_unigene_extension()))
    print(file)
    if my_io.is_valid_gene_file_name(file):
        # using f-strings
        print(f"\nFound Gene {gene} for {host}")
    else:
        print("Not found", file=sys.stderr)
        print(f"Gene {gene} does not exist for {host}. exiting now...", file=sys.stderr)
        sys.exit()
    get_gene_data(file)


