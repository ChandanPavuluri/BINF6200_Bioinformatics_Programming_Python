import re
import sys
import argparse


def args_parse():
    """Function for arguments"""

    parser = argparse.ArgumentParser(description='Give the fasta sequence file name to do the splitting')
    parser.add_argument('-i', '--infile', dest='INFILE', help='Path to the file to open', required=True)

    return parser.parse_args()


def get_fh(input_file, read_write):
    """Function for opening the file"""

    try:
        return open(input_file, read_write)
    except IOError:
        raise IOError
    except ValueError:
        raise Exception("Error wrong open mode entered it should be r or w")


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
        sys.exit("The size of the sequences and the header lists is different \n"
                 "Are you sure the FASTA is in correct format")
    else:
        return True


def main():

    args = args_parse()
    fh_in = get_fh(args.INFILE, "r")
    list_headers, list_seqs = get_header_and_sequence_lists(fh_in)
    protein = get_fh("pdb_protein.fasta", "w")
    sec_str = get_fh("pdb_ss.fasta", "w")
    protein_length = 0
    sec_str_length = 0
    for header, sequence in zip(list_headers, list_seqs):
        if re.search("^>.*sequence", header):
            protein.write(header)
            protein.write("\n")
            protein.write(sequence)
            protein.write("\n")
            protein_length += 1
        elif re.search("^>.*secstr", header):
            sec_str.write(header)
            sec_str.write("\n")
            sec_str.write(sequence)
            sec_str.write("\n")
            sec_str_length += 1
    protein.close()
    sec_str.close()
    print(f"Found {protein_length} protein sequences")
    print(f"Found {sec_str_length} ss sequences")


if __name__ == "__main__":
    main()
