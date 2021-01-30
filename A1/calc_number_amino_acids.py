"""
#!/usr/bin/env python3
#Calc_number_amino_acids.py
"""
import sys
def my_function():
    """Function to disable Uppercase naming convention """
    # Input- Entering the name of DNA sequence
    seq_name = str(input("Please enter a name for the DNA sequence: "))
    #Printing the name of sequence
    print("Your sequence name is:", seq_name)
    # Input- Entering the length of sequence
    seq_length = int(input("Please enter the length of the sequence: "))
    # If-else Condition to check if the sequence is divisible by 3
    if seq_length % 3 == 0:
        # If sequence is divisible by 3 prints the sequence length
        print("The length of the DNA sequence is:", seq_length)
        # Dividing the sequence by 3
        protein = (seq_length/3)
        # Printing the length of the protein
        print("The length of the decoded protein is:", float(protein))
        # Printing the average weight of the sequence
        print(f"The average weight of protein sequnce is: {(protein*110)/1000:0.2f}")

    else:
        # If the sequence is not a divisible of 3 it exits
        print('Error: the DNA sequence is not a multiple of 3"')
        sys.exit()

if __name__ == "__main__":
    my_function()
