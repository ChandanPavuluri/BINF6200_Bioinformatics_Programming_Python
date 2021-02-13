import sys
import math

data=[]
column=[]
na=[]

def min_max():
    column.sort()
    minimum = column[0]
    maximum = column[-1]
    print("Maximum = {:.3f}".format(maximum))
    print("Minimum = {:.3f}".format(minimum))


def Variance():
    var = []
    for num in column:
       var.append((num - Average)**2)
    try:
        Variance = sum(var)/(ValidNum-1)
    except ZeroDivisionError:
        Variance = 0
    print("Variance = {:.3f}".format(Variance))
    Std_Dev = math.sqrt(Variance)
    print("Std Dev = {:.3f}".format(Std_Dev))

def Median():
    column.sort()
# Finding the position of the median
    if len(column) % 2 == 0:
        first_median = column[len(column) // 2]
        second_median = column[len(column) // 2 - 1]
        median = (first_median + second_median) / 2
    else:
        median = column[len(column) // 2]

    print("Median = {:.3f}".format(median))
if __name__ == "__main__":

    datafile=sys.argv[1]
    coln=sys.argv[2]

    with open(datafile) as input_file:
        for line in input_file:
            i=1
            try:
                num = line.split("\t")[int(coln)]
                data.append(num)
                i=+1
            except IndexError:
                print("Exiting: There is no valid 'list index' in column {} in line {} in file: {}".format(coln,i,datafile))
                sys.exit()
   # print(data)
    
    removed = 0
    for q,val in enumerate(data):
        try:
            if val in ("NaN","nan"):
                na.append(val)
                removed+=1
            else:
                column.append(float(val))
        except ValueError:
            print("Skipping line number {} : could not convert string to float: '{}'".format(q+1,val))
            removed+= 1
    
    Count = len(column)+removed
    ValidNum = len(column)

    #Calculating Average
    try:
        Average = sum(column)/ValidNum
    except ZeroDivisionError:
        print("Error: There were no valid number(s) in column {} in file: {}".format(coln,datafile))
        sys.exit()


     
    print(coln)

    print("Count = {:.3f}".format(Count))
    print("ValidNum = {:.3f}".format(ValidNum))
    print("Average = {:.3f}".format(Average))
    min_max()
    Variance()
    Median()
