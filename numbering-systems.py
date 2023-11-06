#convert strings to base-10 numbers & base-10 numbers to hexadecimal numbers.
#Credits to Eric Pogue for his numbering systems tutorial

import sys

print("\nNumbering Systems\n")
numberOfArgs = len(sys.argv)
print("Total arguments: " + str(numberOfArgs),"\n")
print("Argument 1: " + sys.argv[0],"\n")

if numberOfArgs == 2:
    print("Argument 2: " + sys.argv[1],"\n")
    numberAsString = sys.argv[1]
    numberAsInt = int(numberAsString, base=10)
    numberAsHex = hex(numberAsInt)

    print("Input: " + numberAsString,"\n")
    print("Base-10: " + str(numberAsInt),"\n")
    print("Hexadecimal: " + numberAsHex,"\n")