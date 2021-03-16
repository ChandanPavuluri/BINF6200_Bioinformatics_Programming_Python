

import argparse
import collections
import re
import os
from assignment4 import my_io

'''
The following program takes two input and outputs a file that contains category, occurrence,
and description.
'''
def get_occurrence(infile1):
    '''
    Function takes input file and splits at the tab delimited and returns dictionary of categories and occurrence of those categories.
    '''
    counts = collections.defaultdict(int)
    sorted_count = {} # initializing empty dictionary 
    d = {line.split('\t')[0]: line.rstrip('\n').split('\t')[2] for line in infile1}
    print(d)
    for key, val in d.items():
        if re.findall("\d+", val):
        #if re.match("[0-9]\.?", val): # searching int and floats
            counts[val] += 1
    print(counts)
    for i in sorted(counts): # sorting in ascending order
        sorted_count[i] = counts[i]
    print(sorted_count)
    return sorted_count

def get_gene_description(infile2):
    '''
    Function takes input file and splits at the tab delimited and returns dictionary of categories and description.
    '''
    des_ = {} # initializing an empty dictionary 
    dd = {line.strip().split('\t')[0]: line.strip().split('\t')[1] for line in infile2}
    print("knoe")
    print(dd)
    for key, val in dd.items():
        des_[key] = val
    print(des_)
    return des_
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Combine on gene name and count the category occurrence')
    parser.add_argument('-i1','--infile1', dest='infile1', type=str, help='Path to the gene description file to open', required=False)
    parser.add_argument('-i2','--infile2', dest='infile2', type=str, help='Path to the gene category to open', required=False)
    args = parser.parse_args()
    if args.infile1 and args.infile2:
        infile1 = my_io.get_fh(args.infile1, 'r')
        infile2 = my_io.get_fh(args.infile2, 'r')
    else:
        print("Wrong input/or non given, proceeding with default files :'chr21_genes.txt' and 'chr21_genes_categories.txt'")
        infile1 = open('chr21_genes.txt', 'r')
        infile2 = open('chr21_genes_categories.txt', 'r')

    gene_count = get_occurrence(infile1)
    gene_desc = get_gene_description(infile2)
    get_occurrence(infile1)
    get_gene_description(infile2)
    output = "OUTPUT/categories.txt"
    outfile = my_io.get_fh(output, 'w')
    outfile_header = ("Category","Occurrence","Description","\n")
    outfile.write("\t".join(outfile_header))
    for i in gene_count:
        try:
            pass
            outfile.write(str(i)+"\t"+str(gene_count[i])+"\t"+gene_desc[i]+"\n")
        except KeyError:
            pass
    infile1.close()
    infile2.close()
