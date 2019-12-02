/*This is a file that contains the function of another file named Array_TIFR.cpp.
This file will be used to test the action of using Makefile
*/

#include <stdlib.h>

float *MuAndVar(int* ref,int n)
{
  float *MuAndVar = (float *)malloc(2*sizeof(float));
  float s1 = 0, s2 = 0;
  for(int i = 0; i<n; i++){
    s1 += ref[i];
    s2 += ref[i]*ref[i];
  }
  MuAndVar[0] = s1/n;
  MuAndVar[1] = s2/n - (s1/n)*(s1/n);

  return MuAndVar;
}
