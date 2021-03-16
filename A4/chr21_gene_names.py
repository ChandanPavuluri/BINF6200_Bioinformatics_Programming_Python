import argparse
import sys
from assignment4 import my_io


def main():
    """Function for calling all the functions """

    args = args_parse()
    fh_in = my_io.get_fh(args.INFILE, "r")
    gene_ids = write_dict(fh_in)
    gene_description(gene_ids)
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
                        required=True)

    return parser.parse_args()


def write_dict(input_file):
    gene_ids_dict = {}
    with input_file as file_handle:
        for line in file_handle:
            line = line.split("\t")
            gene_ids_dict[line[0]] = line[1]
    gene_ids_dict.pop("Gene Symbol")
    print(gene_ids_dict)
    return gene_ids_dict


def _get_case_insensitive_dict(input_dict, key):
    dict_value = next((value for dict_key, value in input_dict.items() if dict_key.lower() == key.lower()), None)
    return dict_value


def gene_description(gene_dict):
    while True:
        gene_name = str(input("Enter gene name of interest. Type quit to exit: "))
        gene_name = gene_name.lower()
        if gene_name == "quit" or gene_name == "exit":
            break
        else:
            dict_value = _get_case_insensitive_dict(gene_dict, gene_name)
            if dict_value is None:
                print("Not a valid gene name.\n")
            else:
                print("\n" + f"{gene_name} found! Here is the description:" + "\n" + f"{dict_value}" + "\n")
    print("Thanks for querying the data.")
    sys.exit()


if __name__ == "__main__":
    main()
