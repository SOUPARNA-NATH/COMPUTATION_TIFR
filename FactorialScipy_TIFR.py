"""This is a program to find out the factorial using the 'factorial' function available in scipy module

Author:- Souparna Nath

Date:- 27/11/2019"""

import scipy.misc as misc

def main():
    n =  int(input("Enter the value: "))
    print("The factorial of ",n,"is: ",misc.factorial(n,exact = True))
    return

main()
