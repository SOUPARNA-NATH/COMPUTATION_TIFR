/* This is a program to calculate factorial using recursion and directly in C

Author: Souparna Nath

Date: 27/11/2019
*/

#include <stdio.h>
#include<time.h>

long factorialD(int);
long factorialR(int);


long factorialD(int n)   //calculating factorial directly
{
  long f = 1;
  for(int i = 2; i<=n; i++)  f *= i;
  return f;
}

long factorialR(int n)   //calculating factorial recursively
{
  if (n == 1) return 1;

  return n*factorialR(n-1);
}

int main()   //calling the main function
{
  int n = 0;
  printf("%s","Enter the value: ");
  scanf("%d\n",&n);
  
  clock_t startR,startD,endR,endD;
  
  startR = clock();
  
  factorialR(n);
  
  endR = clock();

  startD = clock();
  
  factorialD(n);
  
  endD = clock();
  
  double timeR = 1.0*(endR-startR)/CLOCKS_PER_SEC;
  double timeD = 1.0*(endD-startD)/CLOCKS_PER_SEC;
  
  printf("The factorial of %d by recursive way is: %li\n",n,factorialR(n));
  printf("The factorial of %d by direct way is: %li\n",n,factorialD(n));
  printf("The time taken to calculate factorial recursively: %lf\n",timeR);
  printf("The time taken to calculate factorial directly: %lf\n",timeD);
  
  return 0;
}
