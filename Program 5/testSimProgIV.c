#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float surand()
{
return( (float) rand()/RAND_MAX );
}

float urand(float low, float high)
{
return(low+(high-low)*surand());
}

float generatez()
{
float x,y,fx;
while (1)
    {
      x=urand(0,1);
      y=urand(0,3);
      fx=0.33*(x-1)*(x-1);
      if (y<fx)
   {
      break;
   }
   
    }
return(x);
}

void main(int argc, char *argv[])
{
int i,n;
float z;
n=atoi(argv[1]);
for (i=0;i<n;i++)
    {
      z=generatez();
      printf(" %2.4f \n",z);
    }
}