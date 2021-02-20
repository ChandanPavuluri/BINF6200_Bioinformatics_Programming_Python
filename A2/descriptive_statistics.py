"""
Descriptive Statistics and Lists
#descriptive_statistics.py
"""
# importing required modules(sys and math)
import sys
import math


def main():
    """ parsing and cleaning the data"""

    # calculating length of arguments while executing the file
    arg_count = len(sys.argv) - 1

    # if length of the argument count was less than 2 then raise an exception
    if arg_count < 2:
        raise Exception("This script requires 2 arguments: Datafile name and then column number")
    # Arguments needed while executing
    input_datafile = sys.argv[1]
    column_number = sys.argv[2]

    # Creating empty lists for required data
    data = []
    column_data = []

    # Opening and reading the input file and extracting the required data
    with open(input_datafile) as input_file:
        for line in input_file:
            i = 1
            try:
                num = line.split("\t")[int(column_number)]
                data.append(num)
                i = +1
            # If the column number entered is invalid then except the error
            except IndexError:
                print("Exiting: There is no valid 'list index' in column {} in line {} in file: {}"
                      .format(column_number, i, input_datafile))
                sys.exit()

    # Initializing a variable for counting the number of removed values
    removed_value = 0

    # Removing the non numeric values from the required data and converting the values to float
    # and appending to a new list
    for index, value in enumerate(data):
        try:
            if math.isnan(float(value)):
                removed_value += 1
            else:
                column_data.append(float(value))
        # if the value is other than numerical or nan then expect value error.
        except ValueError:
            print("Skipping line number {} : could not convert string to float: '{}'"
                  .format(index + 1, value))
            removed_value += 1

    # Calculating length of total column
    count = len(column_data) + removed_value

    # Calculating length of only numerical values
    valid_number = len(column_data)

    # Calculating Average of the data
    try:
        average = sum(column_data) / valid_number
    except ZeroDivisionError:
        print("Error: There were no valid number(s) in column {} in file: {}"
              .format(column_number, input_datafile))
        sys.exit()
    # Final output print statements
    print()
    print("\t{} {}".format("Column:", column_number))
    print("\n")
    print("\t\t{:<8} {} {:>8.3f}".format("Count", "=", count))
    print("\t\t{:<8} {} {:>8.3f}".format("ValidNum", "=", valid_number))
    print("\t\t{:<8} {} {:>8.3f}".format("Average", "=", average))
    # Calling the functions
    minimum_maximum(column_data)
    variance_stddev(column_data, valid_number, average)
    middle_value(column_data)


def minimum_maximum(column_data):
    """Function for identifying Maximum and Minimum number"""

    # sorting the list in ascending order
    column_data.sort()

    # selecting first value- minimum value
    minimum = column_data[0]

    # selecting the last value- maximum value
    maximum = column_data[-1]

    # Printing maximum and minimum values
    print("\t\t{:<8} {} {:>8.3f}".format("Maximum", "=", maximum))
    print("\t\t{:<8} {} {:>8.3f}".format("Minimum", "=", minimum))


def variance_stddev(column_data, valid_number, average):
    """Function for calculating Variance and Standard Deviation"""

    # creating an empty list
    var = []

    # Calculating Variance
    for number in column_data:
        var.append((number - average) ** 2)
    try:
        variance = sum(var) / (valid_number - 1)
    # If divided by zero or numerator Zero
    except ZeroDivisionError:
        variance = 0

    # printing Variance of data
    print("\t\t{:<8} {} {:>8.3f}".format("Variance", "=", variance))

    # Calculating Standard Deviation
    std_dev = math.sqrt(variance)

    # printing Standard Deviation of data
    print("\t\t{:<8} {} {:>8.3f}".format("Std_Dev", "=", std_dev))


def middle_value(column_data):
    """Function for calculating Median"""

    # sorting the list in ascending order
    column_data.sort()

    # Finding the position of the median
    if len(column_data) % 2 == 0:
        first_middle_value = column_data[len(column_data) // 2]
        second_middle_value = column_data[len(column_data) // 2 - 1]
        median = (first_middle_value + second_middle_value) / 2
    else:
        median = column_data[len(column_data) // 2]

    # printing median of data
    print("\t\t{:<8} {} {:>8.3f}".format("Median", "=", median))


if __name__ == "__main__":
    main()
