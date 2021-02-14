"""
Descriptive Statistics and Lists
#descriptive_statistics.py
"""
import sys
import math

def iterate():

    input_file_name = sys.argv[1]
    column_to_parse = sys.argv[2]

    global DATA
    global COLUMN_DATA
    global NAN 

    DATA = []
    COLUMN_DATA = []
    NAN =[]
    with open(input_file_name) as input_file:
        for line in input_file:
            i = 1
            try:
                num = line.split("\t")[int(column_to_parse)]
                DATA.append(num)
                i = +1
            except IndexError:
                print("Exiting: There is no valid 'list index' in column {} in line {} in file: {}"
                      .format(column_to_parse, i, input_file_name))
                sys.exit()
    global REMOVED_VALUE
    REMOVED_VALUE = 0
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

def count_average():

    # Calculating length of total column
    global COUNT
    COUNT = len(COLUMN_DATA) + REMOVED_VALUE

    # Calculating length of valid Numbers
    global VALIDNUM
    VALIDNUM = len(COLUMN_DATA)

    #Calculating Average
    global AVERAGE
    try:
        AVERAGE = sum(COLUMN_DATA) / VALIDNUM
    except ZeroDivisionError:
        print("Error: There were no valid number(s) in column {} in file: {}"
              .format(column_to_parse, input_file_name))
        sys.exit()
        
    print("{:<4} {}".format("Column:", column_to_parse))
    print("{:<10}{}{:>10.3f}".format("Count", "=", COUNT))
    print("{:<10}{}{:>10.3f}".format("ValidNum", "=", VALIDNUM))
    print("{:<10}{}{:>10.3f}".format("Average", "=", AVERAGE))


def min_max():
    """Function for identifying Maximum and Minimum number"""
    column_data.sort()
    minimum = column_data[0]
    maximum = column_data[-1]
    print("{:<10}{}{:>10.3f}".format("Maximum", "=", maximum))
    print("{:<10}{}{:>10.3f}".format("Minimum", "=", minimum))

def variance_stddev():
    """Function for calculating Variance and Standard Deviation"""
    var = []
    for number in column_data:
        var.append((number - Average) ** 2)
    try:
        variance = sum(var) / (ValidNum - 1)
    except ZeroDivisionError:
        variance = 0
    print("{:<10}{}{:>10.3f}".format("Variance", "=", variance))
    std_dev = math.sqrt(variance)
    print("{:<10}{}{:>10.3f}".format("Std_Dev", "=", std_dev))

def statistics():
    """Function for calculating Median"""
    column_data.sort()
    # Finding the position of the median
    if len(column_data) % 2 == 0:
        first_value = column_data[len(column_data) // 2]
        second_value = column_data[len(column_data) // 2 - 1]
        median = (first_value + second_value) / 2
    else:
        median = column_data[len(column_data) // 2]
    print("{:<10}{}{:>10.3f}".format("Median", "=", median))

if __name__ == "__main__":
    ARG_COUNT = len(sys.argv) - 1
    # if length of the argument count was less than 2 we need to raise an exception
    if ARG_COUNT < 2:
        raise Exception("This script requires 2 arguments: Datafile name and then column number")

    
    iterate()
    count_average()
    min_max()
    variance_stddev()
    statistics()
