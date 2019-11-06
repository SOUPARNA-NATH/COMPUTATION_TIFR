"""
This is a program to generate n Fibonacci Numbers

Author:- Souparna Nath

Date:- 05.11.2019
"""

def FibonacciGenerate(n):
    
    first = 0
    second = 1
    
    Fib = []
    Fib.extend([first,second])
    
    for i in range(n-2):
        third = first + second
        Fib.append(third)
        first = second
        second = third
    return Fib
