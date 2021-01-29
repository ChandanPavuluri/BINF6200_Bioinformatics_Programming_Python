#!/usr/bin/env python3

def main():
    a= int(input("Enter first number:"))
    b=int(input("Enter second number:"))

    while b != 0:
        if a>b:
            a=a-b
            print("first a:", a)
        else:
            b=b-a
            print("B:", b)
    print("The GCD of the number is ",a)

main()
