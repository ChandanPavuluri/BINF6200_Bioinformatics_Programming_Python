"""
nucleotide_statistics_from_fasta.py.py
#nucleotide_statistics_from_fasta.py.py
"""

# importing required modules
import re
import sys
import argparse


def main():
    """Function for calling all the functions """

    args = args_parse()
    fh_in = get_fh(args.INFILE, "r")
    list_headers, list_seqs = get_header_and_sequence_lists(fh_in)
    fh_out = get_fh(args.OUTFILE, "w")
    print_sequence_stats(list_headers, list_seqs, fh_out)


def args_parse():
    """Function for arguments"""

    # Creating argument parser object
    parser = argparse.ArgumentParser(description='Give the fasta sequence file name'
                                                 ' to get the nucleotide statistics')

    # adding arguments that are needed
    parser.add_argument('-i', '--infile', dest='INFILE', help='Path to the file to open',
                        required=True)
    parser.add_argument('-o', '--outfile', dest='OUTFILE', help='Path to the file to write',
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


def print_sequence_stats(headers, seqs, output):
    """ Writing the sequence stats to a txt file """

    # Creating variables for the index
    index = 0

    # writing the header to the output file
    output.write('\t'.join(["Number", "Accession", "A's", "G's", "C's", "T", "N's", "Length",
                            "GC%"]) + '\n')

    # zipped the headers and sequence lists to get the accession number and counts of the bases
    for header_string, seq in zip(headers, seqs):
        index += 1
        accession_string = _get_accession(header_string)

        # Calling the function for counting bases
        num_a = _get_nt_occurrence("A", seq)
        num_g = _get_nt_occurrence("G", seq)
        num_c = _get_nt_occurrence("C", seq)
        num_t = _get_nt_occurrence("T", seq)
        num_n = _get_nt_occurrence("N", seq)

        # Calculating the total bases in sequences
        length = num_a + num_g + num_c + num_t + num_n

        # Calculating the GC content
        gc_content = round(((num_g + num_c) / length) * 100, 1)

        # creating the format for the lines of out file
        statistics = [str(index), str(accession_string), str(num_a), str(num_g), str(num_c),
                      str(num_t), str(num_n), str(length), str(gc_content)]

        # writing every accessions statistics to the out file
        output.write('\t'.join(statistics) + '\n')

    # printing the statistics
    # print('\t'.join(statistics) + '\n')

    # returning the last statistics for testing
    return statistics


def _get_nt_occurrence(nt_base, sequence):
    """ Calculates the nucleotide occurance in each sequence"""
    count = 0

    # list of bases to be considered
    bases = ["A", "G", "T", "C", "N"]
    if nt_base in bases:
        for nucleotides in sequence:
            if nt_base in nucleotides:
                count += 1
    else:
        sys.exit("Did not code this condition")

    # returning the total count of bases in each sequence
    return count


def _get_accession(header):
    """ Getting the accession number from header line """

    # splitting the header line after first space and keeping only before space and removing '>'
    header = header.split(" ")
    header = header[0]
    accession = re.sub(">", "", header)

    # returns accession number
    return accession


if __name__ == "__main__":
    main()
