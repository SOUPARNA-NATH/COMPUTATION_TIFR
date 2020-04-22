/*This is a program to solve initial value problem using Euler's Method

Author:- Souparna Nath

Date:- 19/04/20
*/

#include <stdio.h>
#include <math.h>

double f(double,double);
double y_exact(double);


double f(double t,double y)
{
  return y-t*t + 1;
}


double y_exact(double t)
{
  return (t+1)*(t+1) - 0.5*exp(t);
}


int main()
{
  int a = 0;
  int b = 2;
  double y0 = 0.5;
  double h = 0.01;
  int N = 100*(b-a);

  double y_n[N];
  double err[N];
  double err_bound[N];

  y_n[0] = y0;

  for (int i = 1; i<=N; i++){
    double ynew = y0 + h*f(a+(i-1)*h,y0);
    y_n[i] = ynew;
    y0 = ynew;
  }


  for (int j = 0; j<N; j++){
    err[j] = y_n[j] - y_exact(a+j*h);

    /*Local Error Bound is defined as 1/2*M*dt, where M is the bound on
    y''(t) at t = some t0.
    Now, y''(t) = y' - 2t = y -t^2 -2t +1 = y +2 -(t+1)^2
    (t +1)^2 <= 0, Implies |y''| <= y+2 = M.
    y is known. 
    Hence, y(t)+ 2 = M
    */
    double M = y_exact(a+j*h)+2;
    
    err_bound[j] = 0.5*M*h;
  }


  printf("t\tApproximate Value\tExact Value\tRelative Error\tError Bound\n");
  for (int k = 0; k<N; k++){
    printf("%lf\t%lf\t%lf\t%lf\t%lf\n",k*h,y_n[k],y_exact(k*h),err[k],err_bound[k]);
  }
  return 0;
}
