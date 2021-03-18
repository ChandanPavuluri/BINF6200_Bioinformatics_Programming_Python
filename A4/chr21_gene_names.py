import argparse
import sys
from assignment4 import my_io


def main():
    """Function for calling all the functions """

    args = args_parse()
    fh_in = my_io.get_fh(args.INFILE, "r")
    gene_ids_dict = write_dict(fh_in)
    gene_description(gene_ids_dict)
    fh_in.close()


def args_parse():
    """
    Function for command line arguments
    @return: Instance of argparse arguments
    """

    # Creating argument parser object
    parser = argparse.ArgumentParser(description='Open chr21_genes.txt, and ask '
                                                 'user for a gene name')

    # adding arguments that are needed
    parser.add_argument('-i', '--infile', dest='INFILE', help='Path to the file to open',
                        default="chr21_genes.txt")

    return parser.parse_args()


def write_dict(input_file):
    """
        Function for creating the gene symbol and description dictionary
        @param input_file: File handle of the opened input file of genes
        @return: returning the dictionary
    """

    # Initializing the empty list
    gene_ids_dict = {}
    with input_file as file_handle:
        for line in file_handle:
            line = line.split("\t")
            gene_ids_dict[line[0]] = line[1]

    # Removing the header from the dictionary
    gene_ids_dict.pop("Gene Symbol")

    # Returning the dictionary
    return gene_ids_dict


def _get_case_insensitive_dict(input_dict, key):
    """
        Function for creating a key case insensitive search
        @param input_dict: Input of gene symbol and description dictionary
        @param key: Input of the search element
        @return: returning the dictionary value
    """
    # Helps in searching case insensitive key for dictionary by converting the
    # given key to lower and making all the dict keys to lower
    dict_value = next((value for dict_key, value in input_dict.items()
                       if dict_key.lower() == key.lower()), None)
    return dict_value


def gene_description(gene_dict):
    """
            Function for creating a key case insensitive search
            @param gene_dict: Input of gene symbol and description dictionary
            @return: returning the dictionary value
        """
    # Creating an indefinite loop until user enters quit or exit irrespective of case
    while True:
        gene_name = str(input("\nEnter gene name of interest. Type quit to exit: "))

        # When user enters gene_name other than quit then it searches in dictionary
        if gene_name.lower() == "quit" or gene_name.lower() == "exit":
            break
        else:
            dict_value = _get_case_insensitive_dict(gene_dict, gene_name)

            # when given key is not in dictionary it prints not a valid gene
            # else prints description of given gene
            if dict_value is None:
                print("Not a valid gene name.\n", file=sys.stdout)
            else:
                print("\n" + f"{gene_name} found! Here is the description:"
                      + "\n" + f"{dict_value}" + "\n", file=sys.stdout)

    # When user enters quit it prints message and exits out
    print(f"Thanks for querying the data.", file=sys.stdout)
    sys.exit()


if __name__ == "__main__":
    main()
