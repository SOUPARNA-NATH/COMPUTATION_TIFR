/*This is a program to store a list of numbers in an array and to compute its mean and variance.

Author :- Souparna Nath

Date :- 02/12/2019
*/

#include "Array_Header_TIFR.h"

int *ptr =  (int *)calloc(100,sizeof(int));

struct MuAndVar {float mu, var;};


int main()
{
  FILE *f = fopen("/home/alnath/Desktop/COMPUTATION_TIFR/ArrayTest.bin","wb");
  
  struct MuAndVar muvar;
  
  printf("The elements of the array before assigning value: \n");
  for(int i = 0; i<100; i++){
    printf("%d\n",ptr[i]);
  }
  
  for(int i = 0; i<100; i++){
  ptr[i] = (i+1)*(i+1);
  }
  
  muvar.mu = MuAndVar(ptr,100)[0];
  muvar.var = MuAndVar(ptr,100)[1];

  fwrite(&muvar,sizeof(struct MuAndVar),1,f);
  
  free(ptr);
  fclose(f);
  
  return 0;
}
