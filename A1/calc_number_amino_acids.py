"""
#!/usr/bin/env python3
#Calc_number_amino_acids.py
"""
import sys

SEQ_NAME = str(input("Please enter a name for the DNA sequence: "))

print("Your sequence name is:", SEQ_NAME)

SEQ_LENGTH = int(input("Please enter the length of the sequence: "))

if SEQ_LENGTH % 3 == 0:
    print("The length of the DNA sequence is:", SEQ_LENGTH)
    PROTEIN = (SEQ_LENGTH/3)
    print("The length of the decoded protein is:", float(PROTEIN))
    print(f"The average weight of protein sequnce is: {(PROTEIN*110)/1000:0.2f}")

else:
    print('Error: the DNA sequence is not a multiple of 3"')
    sys.exit()
