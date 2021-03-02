"""
pdb_fasta_splitter.py
#pdb_fasta_splitter.py
"""

# Importing required modules
import re
import sys
import argparse


def main():
    """Function for calling all the functions """

    args = args_parse()
    fh_in = get_fh(args.INFILE, "r")
    list_headers, list_seqs = get_header_and_sequence_lists(fh_in)
    protein_count, ss_count = file_write(list_headers, list_seqs)
    print(f"Found {protein_count} protein sequences\nFound {ss_count} ss sequences")


def args_parse():
    """Function for commandline options"""

    # Creating argument parser object
    parser = argparse.ArgumentParser(description='Give the fasta sequence file name '
                                                 'to do the splitting')

    # adding arguments that are needed
    parser.add_argument('-i', '--infile', dest='INFILE', help='Path to the file to open',
                        required=True)

    return parser.parse_args()


def get_fh(input_file, read_write):
    """Function for opening the file"""

    # using try and except to catch the errors if its an IOError and ValueError
    try:
        file_to_open = open(input_file, read_write)
        return file_to_open
    except IOError:
        raise IOError from None
    except ValueError:
        raise ValueError


def get_header_and_sequence_lists(input_file):
    """ Parsing over the input file and creating lists for headers and sequences"""

    # creating empty lists
    headers = []
    seqs = []
    seq_lines = ""
    with input_file as file_handle:
        for line in file_handle:

            # if the line starts with '>' append to headers list else join the seq lines and iterate
            # the remaining lines and keep adding to the string, after adding second header append
            # the sequence lines to sequence list
            if re.search(r"^>", line):
                line = line.replace('\n', "")
                headers.append(line)
                seqs.append(seq_lines)
                seq_lines = ""
            else:
                line = line.replace('\n', "")
                seq_lines = seq_lines + line

    # the last sequence line cannot be appended as there were no headers so we are appending it
    # to the sequence list
    if len(seq_lines) > 0:
        seqs.append(seq_lines)

    # removing the first empty string from sequence list
    seqs.pop(0)

    # calling the function to check if headers and sequence list sizes are equal
    _check_size_of_lists(headers, seqs)

    # return headers and sequence list using iyt for testing
    return headers, seqs


def _check_size_of_lists(headers, seqs):
    """ Check if the lists are of equal size """

    # if lists are of not equal size exit the program by displaying message
    if len(headers) != len(seqs):
        sys.exit("The size of the sequences and the header lists is different \n"
                 "Are you sure the FASTA is in correct format")
    else:
        return True


def file_write(headers, seqs):
    """ Writing two separate files for amino acid sequence and secondary structures"""

    # Creating files for protein and secondary structures
    protein = get_fh("pdb_protein.fasta", "w")
    sec_str = get_fh("pdb_ss.fasta", "w")

    # Creating variables for the counts
    protein_length = 0
    sec_str_length = 0

    # Iterating by zipping both the lists
    for header, sequence in zip(headers, seqs):

        # If sequence word is present in headers then header and sequence of same index
        # append to the files
        if re.search(".*sequence", header):
            protein.write(header)
            protein.write("\n")
            protein.write(sequence)
            protein.write("\n")
            protein_length += 1
        elif re.search(".*secstr", header):
            sec_str.write(header)
            sec_str.write("\n")
            sec_str.write(sequence)
            sec_str.write("\n")
            sec_str_length += 1

    # Closing the files
    protein.close()
    sec_str.close()

    # Returns the counts of the sequences
    return protein_length, sec_str_length


if __name__ == "__main__":
    main()
