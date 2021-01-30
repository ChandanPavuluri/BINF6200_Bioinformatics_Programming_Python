"""
#!/usr/bin/env python3
#calc_daltons.py
"""
def my_function():
    """Function to disable Uppercase naming convention """

    # Hard-coding the protein sequence
    protein = '''MADPAAGPPPSEGEESTVRFARKGALRQKNVHEVKNHKFTARFFKQPTFCSHCTDFIWGFGKQGFQCQVC
CFVVHKRCHEFVTFSCPGADKGPASDDPRSKHKFKIHTYSSPTFCDHCGSLLYGLIHQGMKCDTCMMNVH
KRCVMNVPSLCGTDHTERRGRIYIQAHIDREVLIVVVRDAKNLVPMDPNGLSDPYVKLKLIPDPKSESKQ
KTKTIKCSLNPEWNETFRFQLKESDKDRRLSVEIWDWDLTSRNDFMGSLSFGISELQKAGVDGWFKLLSQ
EEGEYFNVPVPPEGSEGNEELRQKFERAKIGQGTKAPEEKTANTISKFDNNGNRDRMKLTDFNFLMVLGK
GSFGKVMLSERKGTDELYAVKILKKDVVIQDDDVECTMVEKRVLALPGKPPFLTQLHSCFQTMDRLYFVM
EYVNGGDLMYHIQQVGRFKEPHAVFYAAEIAIGLFFLQSKGIIYRDLKLDNVMLDSEGHIKIADFGMCKE
NIWDGVTTKTFCGTPDYIAPEIIAYQPYGKSVDWWAFGVLLYEMLAGQAPFEGEDEDELFQSIMEHNVAY
PKSMSKEAVAICKGLMTKHPGKRLGCGPEGERDIKEHAFFRYIDWEKLERKEIQPPYKPKARDKRDTSNF
DKEFTRQPVELTPTDKLFIMNLDQNEFAGFSYTNPEFVINV'''

    # To get rid of newline characters
    protein = protein.replace('\r', "").replace('\n', "")

    # Calculate the length of Sequence
    amino_acids = len(protein)

    # Prints the statement
    print('The length of "Protein kinase C beta type" is:', str(amino_acids))

    # Calculate the average weight
    average_weight = (amino_acids * 110) / 1000

    # Prints the statement
    print('The average weight of this protein sequence in kilodaltons is:', str(average_weight))

if __name__ == "__main__":
    my_function()
