import re
FASTA = open('myfile.txt', 'r')

headers = []
Seq = []

for line in FASTA:
    if re.search("^>", line):
        headers.append(line)
    else:
        line = line.replace('\n', '')
        Seq.append(line)

for i, seq in zip(headers,Seq):
    length = len(seq)
    print(i, length)
