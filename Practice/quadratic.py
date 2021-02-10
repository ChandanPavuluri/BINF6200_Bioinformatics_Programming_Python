#!/usr/bin/env python3

import math # Makes the math module available.
def main():
    print("This program finds the real solutions to a quadratic")
    print()
    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
    discRoot = (b * b - 4 * a * c)**(1/2)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)
    print()
    print("The solutions are:", root1, root2 )
main()
