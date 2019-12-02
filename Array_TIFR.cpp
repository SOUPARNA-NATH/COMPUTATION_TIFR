/*This is a program to store a list of numbers in an array and to compute its mean and variance.

Author :- Souparna Nath

Date :- 02/12/2019
*/

#include <stdio.h>
#include <stdlib.h>

int *ptr =  (int *)malloc(100*sizeof(int));
float *MuAndVar(int*,int);


int main()
{
  for(int i = 0; i<100; i++){
  ptr[i] = (i+1)*(i+1);
  }

  printf("The mean of the numbers: %f\n",MuAndVar(ptr,100)[0]);
  printf("The variance of the numbers: %f\n",MuAndVar(ptr,100)[1]);

  free(ptr);
  return 0;
}

float *MuAndVar(int *ref,int n)
{
  float *MuAndVar = (float *)malloc(2*sizeof(float));
  float s1 = 0, s2 = 0;
  for(int i=0; i<n; i++){
    s1 += ref[i];
    s2 += ref[i]*ref[i];
  }
  
  MuAndVar[0] = s1/n;
  MuAndVar[1] = s2/n - (s1/n)*(s1/n);

  return MuAndVar;
}
