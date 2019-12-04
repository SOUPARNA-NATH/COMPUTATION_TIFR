/* This is a program to calculate factorial using recursion and directly in C

Author: Souparna Nath

Date: 27/11/2019
*/

#include <stdio.h>

int factorialD(int);
int factorialR(int);

int factorialD(int n)   //calculating factorial directly
{
  int f = 1;
  for(int i = 2; i<=n; i++)  f *= i;
  return f;
}

int factorialR(int n)   //calculating factorial recursively
{
  if (n == 1) return 1;

  return n*factorialR(n-1);
}

int main()   //calling the main function
{
  int n = 0;
  printf("%s","Enter the value: ");
  scanf("%d\n",&n);
  printf("The factorial of %d by recursive way is: %d\n",n,factorialR(n));
  printf("The factorial of %d by direct way is: %d\n",n,factorialD(n));
  return 0;
}
