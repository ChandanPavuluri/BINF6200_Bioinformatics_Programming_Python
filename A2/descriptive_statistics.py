import sys
import re
import collections
data=[]
column=[]
na=[]

def average():
    try:
        avg = sum(column)/int(len(column))
        print("Average = {:.3f}".format(avg)) 
    except ZeroDivisionError:
        print("There were no valid number(s) in column {} in file: {}".format(coln,datafile))
        sys.exit()


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
                print("There is no valid 'list index' in column {} in line {} in file: {}".format(coln,i,datafile))
                sys.exit()
   # print(data)
    
    count=0
    NaN = None
    nan = None
    for q,val in enumerate(data):
        try:
            if (val == "NaN" or val == "nan"):
                na.append(val)
                count+=1
            else:
                column.append(float(val))
        except ValueError:
            print("Skipping line number {} : could not convert string to float: '{}'".format(q+1,val))
            count+= 1

   # print(column) 
    print(coln)
    print(len(column)+count)
    print(len(column))
    average()

  
