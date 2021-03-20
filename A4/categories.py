"""
categories.py
#categories.py
"""

# importing required modules
import argparse
import collections
import re
from assignment4 import my_io


def main():
    """Function for calling all the functions"""

    args = args_parse()
    fh_in = my_io.get_fh(args.INFILE1, "r")
    fh_in2 = my_io.get_fh(args.INFILE2, "r")
    occurrence = occurrence_dict(fh_in)
    description = description_dict(fh_in2)
    outfile = "OUTPUT/categories.txt"
    fh_out = my_io.get_fh(outfile, 'w')
    fh_out_header = ("Category", "Occurrence", "Description", "\n")
    fh_out.write("\t".join(fh_out_header))
    for i in occurrence:
        fh_out.write("\t".join([str(i), str(occurrence[i]), description[i]]) + "\n")

    # Closing all the opened files
    fh_in.close()
    fh_in2.close()
    fh_out.close()


def args_parse():
    """
    Function for command line arguments
    @return: Instance of argparse arguments
    """

    # Creating argument parser object
    parser = argparse.ArgumentParser(description='Combine on gene name and '
                                                 'count the category occurrence')

    # adding arguments that are needed
    parser.add_argument('-i1', '--infile1', dest='INFILE1',
                        help='Path to the gene description file to open',
                        default="chr21_genes.txt")
    parser.add_argument('-i2', '--infile2', dest='INFILE2',
                        help=' Path to the gene category to open',
                        default="chr21_genes_categories.txt")

    return parser.parse_args()


def occurrence_dict(input_file):
    """
        Function for creating the occurrences of categories in to dictionary
        @param input_file: File handle of the opened input file
        @return: returning the Categories dictionary
    """

    # Initializing an empty dictionary
    categories = {}
    with input_file as file_handle:
        for line in file_handle:
            line = line.split("\t")
            line[2] = line[2].replace('\n', "")
            categories[line[0]] = line[2]

    # counts the categories using Counter from collections module
    categories_count_dict = dict(collections.Counter(categories.values()))

    # creating an empty removal list for adding keys other than categories
    removal_items = []

    for key in categories_count_dict:
        # if digit is the key then pass else append the key to the list
        if re.findall(r"\d+", key):
            pass
        else:
            removal_items.append(key)

    # remove the list items from the dictionary
    for key in removal_items:
        categories_count_dict.pop(key)

    # arrange the dictionary in ascending order based on sorted list
    categories_sorted = [(k, categories_count_dict[k]) for k in sorted(categories_count_dict)]

    # convert list to sorted dictionary
    categories_count_dict = dict(categories_sorted)

    # return categories_count_dict
    return categories_count_dict


def description_dict(input_file):
    """
        Function for creating the description of categories in to dictionary
        @param input_file: File handle of the opened description input file
        @return: returning the description dictionary
    """

    # Initializing an empty dictionary
    description = {}
    with input_file as file_handle:
        for line in file_handle:
            line = line.split("\t")
            line[1] = line[1].replace('\n', "")
            description[line[0]] = line[1]

    return description


if __name__ == "__main__":
    main()
