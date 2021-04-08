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
    """Function for calling all the functions """
    args = args_parse()
    gene = args.GENE
    host = modify_host_name(args.HOST)
    temp_host = re.sub("_", " ", host)
    file = "/".join((config.get_unigene_directory(), host, gene + "." +
                     config.get_unigene_extension()))
    check_gene(file, gene, temp_host)
    tissues = get_gene_data(file)
    print_output(temp_host, gene, tissues)


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
    """
        Function for extracting the scientific name from the given name
        @param host_name: user entered host name
        @return: returning the scientific name
    """
    # calling the dictionary of host names from config
    host_dict = config.get_host_keywords()

    # converting user entered hostname to lower case
    host_name = host_name.lower()

    # Removing "_" if user entered host name has "_"
    host_name = re.sub("_", " ", host_name)

    # if host name is not present in the dictionary then call the
    # _print_host_directories() and exit
    # else return the value to the given host name
    if host_name not in host_dict.keys():
        _print_host_directories()
    else:
        scientific_host_name = host_dict[host_name]

    # returns the host name
    return scientific_host_name


def _print_host_directories():
    """
        Function for printing scientific names from the data
    """
    # calling the dictionary of host names from config
    host_dict = config.get_host_keywords()

    # converting the dictionary to set
    scientific_name = set(host_dict.values())

    # converting the set to list
    scientific_name = list(scientific_name)

    print("\nEither the Host Name you are searching for is not in the database")
    print("\nor If you are trying to use the scientific name please put the name in double quotes:")
    print('\n"Scientific name"')
    print("\nHere is a (non-case sensitive) list of available Hosts by scientific name")

    # By using enumerate printing along with index
    for (i, item) in enumerate(scientific_name, start=1):
        print(f"{i:2}. {item}")

    # converting the dict keys to list
    common_name = list(host_dict.keys())

    # sorting the list in order
    common_name.sort()

    print("\nHere is a (non-case sensitive) list of available Hosts by common name")

    # By using enumerate printing along with index
    for (i, item) in enumerate(common_name, start=1):
        item = item.capitalize()
        print(f"{i:2}. {item}")

    sys.exit()


def check_gene(file_name, gene_name, temp_host):
    """
        Function for printing if the gene present or not
        @param file_name: filename generated using join
        @param gene_name: user entered gene name
        @param temp_host: scientific name without "_"
    """
    # if the gene name is present then it is true and prints found
    # else then prints not found and exits the program
    if my_io.is_valid_gene_file_name(file_name):
        print(f"\nFound Gene {gene_name} for {temp_host}")
    else:
        print("Not found")
        print(f"Gene {gene_name} does not exist for {temp_host}. exiting now...", file=sys.stderr)
        sys.exit()


def get_gene_data(file_name):
    """
        Function for extracting the expressed tissues of the given gene
        @param file_name: filename generated using join
        @return: list of tissues

    """

    # creating a file handle and opening the file using my_io.get_fh function
    fh_in = my_io.get_fh(file_name, "r")

    # reading through the lines in file handle
    for line in fh_in:

        # if EXPRESS is found extract that line
        if re.search("EXPRESS", line):

            # replacing the newline character
            line = line.replace("\n", "")

            # removing the capital letters(EXPRESS) from the line
            line = re.sub('[A-Z]', "", line)

            # Splitting the lines at "|" and creating the list
            line_list = line.split("|")

            # removing the space before the elements
            line_list = [element.strip(' ') for element in line_list]

            # sorting the list in alphabetical order
            line_list.sort()

    # returns the sorted list
    return line_list


def print_output(host_name, gene_name, tissue_list):
    """
        Function for printing the output
        @param host_name: temporary host name is given
        @gene_name: user entered gene name
        @tissue_list: list generated from get_gene_data
    """

    # calculates the length of the list
    count = len(tissue_list)

    print(f"In {host_name}, There are {count} tissues that {gene_name} is expressed in:\n")

    # By using enumerate printing along with index
    for (i, item) in enumerate(tissue_list, start=1):
        item = item.capitalize()
        print(f"{i:2}. {item}")


if __name__ == "__main__":
    main()
