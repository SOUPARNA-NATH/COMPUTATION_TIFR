"""This is a program to calculate factorial in python using recursion and directly and call by defining main

Author: Souparna Nath

Date: 27/11/2019"""

import timeit as time

mycode1 = '''
def factorialR(n): #calculating factorial using Recursion
    if (n ==1):
        return 1
    return n*factorialR(n-1)
'''

def factorialR(n): #calculating factorial using Recursion
    if (n ==1):
        return 1
    return n*factorialR(n-1)

mycode2 = '''
def factorialD(n):  #calculating factorial directly
    f = 1
    for i in range(2,n+1):
        f = f*i
    return f
'''

def main():
    n = int(input("Enter the value: "))
    mysetup = ""
    print("The factorial of ",n," is ",factorialR(n))
    print("Time taken for factorial using recursion: ",time.timeit(stmt = mycode1, setup = mysetup, number = 10000))
    print("Time taken for factorial calculated directly: ",time.timeit(stmt = mycode2, setup = mysetup, number = 10000))
    return

main()
