import argparse
import collections
import re
from assignment4 import my_io


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
    categories = {}
    with input_file as file_handle:
        for line in file_handle:
            line = line.split("\t")
            line[2] = line[2].replace('\n', "")
            categories[line[0]] = line[2]

    # counts the categories using Counter from collections module
    categories_count_dict = dict(collections.Counter(categories.values()))

    # creating an empty removal list for adding keys other than categories from the dictionary
    removal_items = []

    for key, val in categories_count_dict.items():
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

    print(categories_count_dict)
    # return categories_count_dict
    return categories_count_dict


def description_dict(input_file):
    description = {}
    with input_file as file_handle:
        for line in file_handle:
            line = line.split("\t")
            line[1] = line[1].replace('\n', "")
            description[line[0]] = line[1]
    print(description)
    return description


args = args_parse()
fh_in = my_io.get_fh(args.INFILE1, "r")
fh_in2 = my_io.get_fh(args.INFILE2, "r")
occur = occurrence_dict(fh_in)
desp = description_dict(fh_in2)
outfile = my_io.get_fh("categories.txt", 'w')
outfile_header = ("Category", "Occurrence", "Description", "\n")
outfile.write("\t".join(outfile_header))
for i in occur:
    try:
        pass
        outfile.write(str(i)+"\t"+str(occur[i])+"\t"+desp[i]+"\n")
    except KeyError:
        pass
fh_in.close()
fh_in2.close()
