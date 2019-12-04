"""This is a program to calculate factorial of the given number using a self designed module in language C

Author: Souparna Nath

Date: 27/11/2019"""

from ctypes import *

fact = CDLL('./fact.so')

def main():  #calling by main
    
    n = int(input("Enter the value: "))
    factD = fact.factorialD(n)
    factR = fact.factorialR(n)
    
    print("The factorial of ",n," calcuated recursively is: ",factR)
    print("The factorial of ",n," calculated directly is: ",factD)
    return

main()
