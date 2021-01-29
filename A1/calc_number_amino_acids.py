#!/usr/bin/env python3
#Calc_number_amino_acids.py
import sys

seq_name = str(input("Please enter a name for the DNA sequence: "))

print("Your sequence name is:",seq_name)

seq_length = int(input("Please enter the length of the sequence: "))

if seq_length % 3 == 0:
    print("The length of the DNA sequence is:",seq_length)
    protein= (seq_length/3)
    print("The length of the decoded protein is:",float(protein))
    print(f"The average weight of protein sequnce is: {(protein*110)/1000:0.2f}")

else:
    print('Error: the DNA sequence is not a multiple of 3"')
    sys.exit()






