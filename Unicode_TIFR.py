"""
This is a program to print characters of a String and its corresponding Unicode
Characters

Author:- Souparna Nath

Date:- 05/11/2019
"""

S = 'mumbai'

#To print the Unicode of a characters in a string

for i in S:
    print(i,ord(i))

#To print the sum of Unicodes

summ = 0

for i in S:
    summ += ord(i)
print()
print("The sum of the numbers is: ",summ)

# To list the Unicodes using List Method

Slist = []

for i in S:
    Slist.append(ord(i))
print()
print("LIST 1: ",Slist)

# To list the Unicodes using List Comprehension
Slist2 = [ord(i) for i in S]
print()
print("LIST 2: ",Slist2)

#To list the Unicodes using Map Method
def Unicode(c):
    return ord(c)
 
Slist3 = map(Unicode,S)
print()
print("LIST 3: ",list(Slist3))
