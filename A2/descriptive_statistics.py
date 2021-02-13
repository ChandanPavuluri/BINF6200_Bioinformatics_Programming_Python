import sys
import math


def min_max():
    column_data.sort()
    minimum = column_data[0]
    maximum = column_data[-1]
    print("Maximum = {:.3f}".format(maximum))
    print("Minimum = {:.3f}".format(minimum))


def Variance_StdDev():
    var = []
    for num in column_data:
        var.append((num - Average)**2)
    try:
        variance = sum(var)/(ValidNum-1)
    except ZeroDivisionError:
        variance = 0
    print("Variance = {:.3f}".format(variance))
    Std_Dev = math.sqrt(variance)
    print("Std Dev = {:.3f}".format(Std_Dev))

def Median():
    column_data.sort()
# Finding the position of the median
    if len(column_data) % 2 == 0:
        first_median = column_data[len(column_data) // 2]
        second_median = column_data[len(column_data) // 2 - 1]
        median = (first_median + second_median) / 2
    else:
        median = column_data[len(column_data) // 2]

    print("Median = {:.3f}".format(median))
if __name__ == "__main__":
    arg_count = len(sys.argv) - 1
    # if length of the argument count was less than 2 we need to raise an exception
    if arg_count < 2:
        raise Exception("This script requires 2 arguments: Datafile name and then column number")

    datafile = sys.argv[1]
    column_number = sys.argv[2]

    data = []
    column_data = []
    nan = []

    with open(datafile) as input_file:
        for line in input_file:
            i = 1
            try:
                num = line.split("\t")[int(column_number)]
                data.append(num)
                i = +1
            except IndexError:
                print("Exiting: There is no valid 'list index' in column {} in line {} in file: {}"
                      .format(column_number, i, datafile))
                sys.exit()
    removed = 0
    for q, val in enumerate(data):
        try:
            if val in ("NaN", "nan"):
                nan.append(val)
                removed += 1
            else:
                column_data.append(float(val))
        except ValueError:
            print("Skipping line number {} : could not convert string to float: '{}'"
                  .format(q+1, val))
            removed += 1

    #Calculating length of total column
    Count = len(column_data)+removed

    #Calculating length of valid Numbers
    ValidNum = len(column_data)

    #Calculating Average
    try:
        Average = sum(column_data)/ValidNum
    except ZeroDivisionError:
        print("Error: There were no valid number(s) in column {} in file: {}"
              .format(column_number, datafile))
        sys.exit()


    print("Column: {}".format(column_number))
    print("Count = {:.3f}".format(Count))
    print("ValidNum = {:.3f}".format(ValidNum))
    print("Average = {:.3f}".format(Average))
    min_max()
    Variance_StdDev()
    Median()
