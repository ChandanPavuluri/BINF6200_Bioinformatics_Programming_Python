import re
import sys
import argparse


def args_parse():
    """Function for arguments"""

    parser = argparse.ArgumentParser(description='Give the fasta sequence file name to get the nucleotide statistics')
    parser.add_argument('-i', '--infile', dest='INFILE', help='Path to the file to open', required=True)
    parser.add_argument('-o', '--outfile', dest='OUTFILE', help='Path to the file to write', required=True)

    return parser.parse_args()


def get_fh(file, read_write):
    """Function for opening the file"""

    try:
        return open(file, read_write)
    except IOError:
        raise IOError from None
    except ValueError:
        raise ValueError


def get_header_and_sequence_lists(input_file):
    headers = []
    seqs = []
    seq_lines = ""
    with input_file as file_handle:
        for line in file_handle:
            if re.search(r"^>", line):
                line = line.replace('\n', "")

                headers.append(line)
                seqs.append(seq_lines)
                seq_lines = ""
            elif re.search(r"[A-Z][\s]", line):
                line = line.replace('\n', "")
                seq_lines = seq_lines + line
        if len(seq_lines) > 0:
            seqs.append(seq_lines)

        seqs.pop(0)
    _check_size_of_lists(headers, seqs)

    return headers, seqs


def _check_size_of_lists(headers, seqs):
    """ Check if the lists are of equal size """
    if len(headers) != len(seqs):
        sys.exit(print("The size of the sequences and the header lists is different \n"
                       "Are you sure the FASTA is in correct format"))
    else:
        return True


def print_sequence_stats(headers, seqs, output):
    index = 0
    output_header = ["Number", "Accession", "A's", "G's", "C's", "T", "N's", "Length", "GC%"]
    output.write('\t'.join(output_header) + '\n')
    for header_string, seq in zip(headers, seqs):
        index += 1
        accession_string = _get_accession(header_string)
        num_a = _get_nt_occurrence("A", seq)
        num_g = _get_nt_occurrence("G", seq)
        num_c = _get_nt_occurrence("C", seq)
        num_t = _get_nt_occurrence("T", seq)
        num_n = _get_nt_occurrence("N", seq)
        length = num_a + num_g + num_c + num_t + num_n
        gc_content = round(((num_g + num_c) / length) * 100, 1)
        statistics = [str(index), str(accession_string), str(num_a), str(num_g), str(num_c),
                      str(num_t), str(num_n), str(length), str(gc_content)]
        print('\t'.join(statistics) + '\n')
        output.write('\t'.join(statistics) + '\n')
    print(statistics)


def _get_nt_occurrence(nt_base, sequence):
    count = 0
    bases = ["A", "G", "T", "C", "N"]
    if nt_base in bases:
        for nucleotides in sequence:
            if nt_base in nucleotides:
                count += 1
    else:
        sys.exit("Did not code this condition")

    return count


def _get_accession(header):

    header = header.split(" ")
    header = header[0]
    accession = re.sub(">", "", header)
    return accession


def main():

    args = args_parse()
    fh_in = get_fh(args.INFILE, "r")
    list_headers, list_seqs = get_header_and_sequence_lists(fh_in)
    fh_out = get_fh(args.OUTFILE, "w")
    print_sequence_stats(list_headers, list_seqs, fh_out)


if __name__ == "__main__":
    main()
