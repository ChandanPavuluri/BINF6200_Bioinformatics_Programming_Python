"""
Descriptive Statistics and Lists
#descriptive_statistics.py
"""
import sys
import math

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
    arg_count = len(sys.argv) - 1
    # if length of the argument count was less than 2 we need to raise an exception
    if arg_count < 2:
        raise Exception("This script requires 2 arguments: Datafile name and then column number")

    INPUT_DATA_FILE = sys.argv[1]
    COLUMN_NUMBER = sys.argv[2]

    DATA = []
    COLUMN_DATA = []
    NAN = []

    with open(INPUT_DATA_FILE) as input_file:
        for line in input_file:
            i = 1
            try:
                num = line.split("\t")[int(COLUMN_NUMBER)]
                data.append(num)
                i = +1
            except IndexError:
                print("Exiting: There is no valid 'list index' in column {} in line {} in file: {}"
                      .format(COLUMN_NUMBER, i, INPUT_DATA_FILE))
                sys.exit()
    removed_value = 0
    for index, value in enumerate(DATA):
        try:
            if value in ("NaN", "nan"):
                nan.append(value)
                removed_value += 1
            else:
                column_data.append(float(value))
        except ValueError:
            print("Skipping line number {} : could not convert string to float: '{}'"
                  .format(index + 1, value))
            removed_value += 1

    # Calculating length of total column
    Count = len(column_data) + removed_value

    # Calculating length of valid Numbers
    ValidNum = len(column_data)

    #Calculating Average
    try:
        Average = sum(column_data) / ValidNum
    except ZeroDivisionError:
        print("Error: There were no valid number(s) in column {} in file: {}"
              .format(COLUMN_NUMBER, DATA_FILE))
        sys.exit()


    print("{:<4} {}".format("Column:", COLUMN_NUMBER))
    print("{:<10}{}{:>10.3f}".format("Count", "=", Count))
    print("{:<10}{}{:>10.3f}".format("ValidNum", "=", ValidNum))
    print("{:<10}{}{:>10.3f}".format("Average", "=", Average))
    min_max()
    variance_stddev()
    statistics()
