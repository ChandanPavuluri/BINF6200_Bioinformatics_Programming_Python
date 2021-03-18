import os

file ='/home/chandan/BINF6200/A1/yy.txt'

try:
    os.path.exists(file)
    os.remove(file)
except OSError as e:
    print("ttTTTTTTTTT",e)


