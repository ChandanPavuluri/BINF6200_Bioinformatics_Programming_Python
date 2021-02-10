import re
my_file = open('myfile.txt', 'r')

sequence = []
headers = []
mydict={}
for line in my_file:
    # Seperate the header
    if re.search(">.*", line):
        headers.append(line)

    elif re.search("^[A-Z]", line):
        sequence.append(line)



for i,seq in enumerate(sequence):
    length=len(seq)
    print(headers[i], length)