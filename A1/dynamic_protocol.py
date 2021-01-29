#!/usr/bin/env python3
#dynamic_protocol.py
# Instruct user how to prepare a 3 ml solution of
# 10 mM NaCl and 0.5 mM MgCl2, given stock solutions
# of 1 M NaCl and 0.1 M MgCl2.

final_vol=int(input("Please enter the final volume of the solution (ml): "))

        # use ml volumes throughout the program

# NaCl
na_cl_stock = int(input("Please enter the NaCl stock (mM): "))
na_cl_final = int(input("Please enter the NaCl final (mM): "))

# concatenation, notice how we are calculating something here!
step1 = "Add " + str(final_vol * (na_cl_final / na_cl_stock)) + " ml NaCl\n";

# MgCl2
mg_stock = int(input("Please enter the MgCl2 stock (mM): "))
mg_final = float(input("Please enter the MgCl2 final (mM): "))

step2 = "Add " + str(final_vol * (mg_final / mg_stock)) + " ml MgCl2\n"

# Water
step3 = "Add water to a final volume of " + str(final_vol) + " ml, and mix\n"

# Protocol, we can then just print things out b/c they have been formatted earlier
print(step1 + step2 + step3)



