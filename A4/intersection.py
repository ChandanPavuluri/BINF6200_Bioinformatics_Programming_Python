import argparse
from assignment4 import my_io


def main():
    args = args_parse()
    fh_in_1 = my_io.get_fh(args.INFILE1, "r")
    fh_in_2 = my_io.get_fh(args.INFILE2, "r")
    infile1_list, infile1_count = create_list(fh_in_1)
    infile2_list, infile2_count = create_list(fh_in_2)
    combined_count, combined_list = join_sort(infile1_list, infile2_list)
    fh_out = my_io.get_fh("intersection_output.txt", "w")
    fh_out.write('\n'.join(combined_list))
    print("\n" + f"Number of unique gene names in {args.INFILE1}: {infile1_count}")
    print(f"Number of unique gene names in {args.INFILE2}: {infile2_count}")
    print(f"Number of common gene symbols found: {combined_count}")
    print("Output stored in OUTPUT/intersection_output.txt")
    fh_in_1.close()
    fh_in_2.close()

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
                        required=True)
    parser.add_argument('-i2', '--infile2', dest='INFILE2', help='Gene list 1 to open',
                        required=True)

    return parser.parse_args()


def create_list(input_file):
    gene_list = []
    with input_file as file_handle:
        for line in file_handle:
            gene_symbol = line.split("\t")[0]
            gene_list.append(gene_symbol)
    gene_list.pop(0)
    gene_list.sort()
    gene_set = set(gene_list)
    count = len(gene_set)
    gene_list = list(gene_set)
    return gene_list, count


def join_sort(list_1, list_2):
    unique = set(list_1).intersection(list_2)
    count = len(unique)
    joint_list = list_1 + list_2
    joint_list.sort()

    return count, joint_list


if __name__ == "__main__":
    main()