"""
intersection.py
#intersection.py
"""

import argparse
import sys
from assignment4 import my_io


def main():
    """Function for calling all the functions and printing the output"""

    args = args_parse()
    fh_in_1 = my_io.get_fh(args.INFILE1, "r")
    fh_in_2 = my_io.get_fh(args.INFILE2, "r")
    infile1_list, infile1_count = create_list(fh_in_1)
    infile2_list, infile2_count = create_list(fh_in_2)
    combined_count, combined_list = join_sort(infile1_list, infile2_list)
    fh_out = my_io.get_fh("OUTPUT/intersection_output.txt", "w")
    fh_out.write('\n'.join(combined_list))
    print("\n" + f"Number of unique gene names in {args.INFILE1}: {infile1_count}", file=sys.stdout)
    print(f"Number of unique gene names in {args.INFILE2}: {infile2_count}", file=sys.stdout)
    print(f"Number of common gene symbols found: {combined_count}", file=sys.stdout)
    print("Output stored in OUTPUT/intersection_output.txt", file=sys.stdout)

    # Closing all the opened files
    fh_in_1.close()
    fh_in_2.close()
    fh_out.close()


def args_parse():
    """
    Function for command line arguments
    @return: Instance of argparse arguments
    """

    # Creating argument parser object
    parser = argparse.ArgumentParser(description='Provide two gene list (ignore header line), '
                                                 'find intersection')

    # adding arguments that are needed
    parser.add_argument('-i1', '--infile1', dest='INFILE1', help='Gene list 1 to open',
                        default="chr21_genes.txt")
    parser.add_argument('-i2', '--infile2', dest='INFILE2', help='Gene list 1 to open',
                        default="HUGO_genes.txt")

    return parser.parse_args()


def create_list(input_file):
    """
    Function for creating list for input files
    @param input_file: File handle of the opened input file
    @return gene_list and length of the list
     """

    # Initializing an empty list
    gene_list = []
    with input_file as file_handle:
        for line in file_handle:
            gene_symbol = line.split("\t")[0]
            gene_list.append(gene_symbol)
    gene_list.pop(0)

    # set helps in taking only unique values
    gene_set = set(gene_list)

    # calculating the length of the set
    count = len(gene_set)

    # Converting the set to list
    gene_list = list(gene_list)

    # returning the gene_list and count
    return gene_list, count


def join_sort(list_1, list_2):
    """
    Function for joining two lists
    @param list_1: first file list
    @param list_2: second file list
    @return common elements count and joined list
     """
    # set() the larger list and then use function called interscetion() to
    # compute the intersected list
    common = set(list_1).intersection(list_2)

    # Calculating the count of intersected list
    count = len(common)

    # Joining the two lists
    joint_list = list_1 + list_2

    # Sorting the joined list
    joint_list.sort()

    # returning the common elements count and Joined list
    return count, joint_list


if __name__ == "__main__":
    main()
