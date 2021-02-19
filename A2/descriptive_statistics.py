"""
Descriptive Statistics and Lists
#descriptive_statistics.py
"""
#importing required modules(sys and math)
import sys
import math


def minimum_maximum():
    """Function for identifying Maximum and Minimum number"""

    #sorting the list in ascending order
    COLUMN_DATA.sort()

    #selecting first value- minimum value
    minimum = COLUMN_DATA[0]

    #selecting the last value- maximum value
    maximum = COLUMN_DATA[-1]

    #Printing maximum and minumum values
    print("{:<8} {} {:>8.3f}".format("Maximum", "=", maximum))
    print("{:<8} {} {:>8.3f}".format("Minimum", "=", minimum))

def variance_stddev():
    """Function for calculating Variance and Standard Deviation"""

    #creating an empty list
    var = []

    #Calculating Variance
    for number in COLUMN_DATA:
        var.append((number - AVERAGE) ** 2)
    try:
        variance = sum(var) / (VALIDNUM - 1)
    except ZeroDivisionError:
        variance = 0

    #printing Variance of data
    print("{:<8} {} {:>8.3f}".format("Variance", "=", variance))

    #Calculating Standard Deviation
    std_dev = math.sqrt(variance)

    #printng Standard Deviation of data
    print("{:<8} {} {:>8.3f}".format("Std_Dev", "=", std_dev))

def middle_value():
    """Function for calculating Median"""

    #sorting the list in ascending order
    COLUMN_DATA.sort()

    # Finding the position of the median
    if len(COLUMN_DATA) % 2 == 0:
        first_middle_value = COLUMN_DATA[len(COLUMN_DATA) // 2]
        second_middle_value = COLUMN_DATA[len(COLUMN_DATA) // 2 - 1]
        median = (first_middle_value + second_middle_value) / 2
    else:
        median = COLUMN_DATA[len(COLUMN_DATA) // 2]

    #printing median of data
    print("{:<8} {} {:>8.3f}".format("Median", "=", median))

if __name__ == "__main__":

    #calculating length of arguments while executing the file
    ARG_COUNT = len(sys.argv) - 1

    # if length of the argument count was less than 2 then raise an exception
    if ARG_COUNT < 2:
        raise Exception("This script requires 2 arguments: Datafile name and then column number")
    # Arguments needed while executing
    INPUT_DATA_FILE = sys.argv[1]
    COLUMN_NUMBER = sys.argv[2]

    # Creating empty lists for required data and "NAN" numbers extraction
    DATA = []
    COLUMN_DATA = []
    NAN = []

    # Opening and reading the input file and extracting the required data
    with open(INPUT_DATA_FILE) as input_file:
        for line in input_file:
            i = 1
            try:
                num = line.split("\t")[int(COLUMN_NUMBER)]
                DATA.append(num)
                i = +1
            except IndexError:
                print("Exiting: There is no valid 'list index' in column {} in line {} in file: {}"
                      .format(COLUMN_NUMBER, i, INPUT_DATA_FILE))
                sys.exit()

    #Initializing a vriable for counting the number of removed values
    REMOVED_VALUE = 0

    # Removing the non numeric values from the required data and converting the values to float
    # and appending to a new list
    for index, value in enumerate(DATA):
        try:
            if value in ("NaN", "nan"):
                NAN.append(value)
                REMOVED_VALUE += 1
            else:
                COLUMN_DATA.append(float(value))
        except ValueError:
            print("Skipping line number {} : could not convert string to float: '{}'"
                  .format(index + 1, value))
            REMOVED_VALUE += 1

    # Calculating length of total column
    COUNT = len(COLUMN_DATA) + REMOVED_VALUE

    # Calculating length of only numerical values
    VALIDNUM = len(COLUMN_DATA)

    # Calculating Average of the data
    try:
        AVERAGE = sum(COLUMN_DATA) / VALIDNUM
    except ZeroDivisionError:
        print("Error: There were no valid number(s) in column {} in file: {}"
              .format(COLUMN_NUMBER, INPUT_DATA_FILE))
        sys.exit()
    #Final output print statements
    print("{:<4} {}".format("Column:", COLUMN_NUMBER))
    print("{:<8} {} {:>8.3f}".format("Count", "=", COUNT))
    print("{:<8} {} {:>8.3f}".format("ValidNum", "=", VALIDNUM))
    print("{:<8} {} {:>8.3f}".format("Average", "=", AVERAGE))
    #Calling the functions
    minimum_maximum()
    variance_stddev()
    middle_value()