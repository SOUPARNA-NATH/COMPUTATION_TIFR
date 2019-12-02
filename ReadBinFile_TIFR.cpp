/*This is a program to read binary file using C

Author:- Souparna Nath

Date:- 03/12/2019
*/

#include <stdio.h>

struct MuAndVar{float mu, var;};

int main()
{
  FILE *f = fopen("/home/alnath/Desktop/COMPUTATION_TIFR/ArrayTest.bin","rb");

  struct MuAndVar muvar;

  fread(&muvar,sizeof(struct MuAndVar),1,f);
  printf("The Mean of the numbers: %f\n",muvar.mu);
  printf("The Variance of the numbers: %f\n",muvar.var);

  return 0;
}
