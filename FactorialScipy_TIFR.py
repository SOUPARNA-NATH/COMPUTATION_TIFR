"""This is a program to find out the factorial using the 'factorial' function available in scipy module

Author:- Souparna Nath

Date:- 27/11/2019"""

import timeit as time
import scipy.misc as misc

def main():
    mysetup = '''import scipy.misc as misc
n =  int(input("Enter the value: "))'''
    
    mycode = '''misc.factorial(n,exact = True)'''

    n = int(input("Enter the value: "))
    
    print("The factorial of ",n,"is: ",misc.factorial(n,exact = True))
    print("Time taken to calculate factorial using SciPy: ",time.timeit(stmt = mycode, setup = mysetup, number = 10000))
    return

main()
