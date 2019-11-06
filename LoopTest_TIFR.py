"""
This is a program to test loops

Author: Souparna Nath

Date:- 05.11.2019
"""

try:
    print([1/i for i in range(6)])
except ZeroDivisionError:
    print("You can't divide by zero. It's undefined")
except:
    print("Unidentified error occured")
finally:
    print()
