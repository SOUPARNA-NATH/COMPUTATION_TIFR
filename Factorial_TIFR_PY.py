"""This is a program to calculate factorial in python using recursion and directly and call by defining main

Author: Souparna Nath

Date: 27/11/2019"""

def factorialR(n): #calculating factorial using Recursion
    if (n ==1):
        return 1
    return n*factorialR(n-1)

def factorialD(n):  #calculating factorial directly
    f = 1
    for i in range(2,n+1):
        f = f*i
    return f

def main():
    n = int(input("Enter the value: "))
    print("The factorial calculated recursively is: ",factorialR(n))
    print("The factorial calculated directly is: ",factorialD(n))
    return

main()
