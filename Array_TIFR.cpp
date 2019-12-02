/*This is a program to store a list of numbers in an array and to compute its mean and variance.

Author :- Souparna Nath

Date :- 02/12/2019
*/

#include "Array_Header_TIFR.h"

int *ptr =  (int *)calloc(100,sizeof(int));

FILE *f = fopen("/home/alnath/Desktop/COMPUTATION_TIFR/ArrayTest.txt","w");

int main()
{
  printf("The elements of the array before assigning value: \n");
  for(int i = 0; i<100; i++){
    printf("%d\n",ptr[i]);
  }
  
  for(int i = 0; i<100; i++){
  ptr[i] = (i+1)*(i+1);
  }

  fprintf(f,"The mean of the numbers: %f\n",MuAndVar(ptr,100)[0]);
  fprintf(f,"The variance of the numbers: %f\n",MuAndVar(ptr,100)[1]);
  
  free(ptr);
  fclose(f);
  
  return 0;
}
