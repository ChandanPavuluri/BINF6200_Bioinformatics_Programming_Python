#!/usr/bin/env python3
#Python test

name = input("ENter file: ")
handle = open(name ,"r")
#handle="Chandan Krishna Pavuluri"
counts= dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) +1

bigcount=None
bigword =None
for word, count in counts.items():
    if bigcount == None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword,bigcount)
