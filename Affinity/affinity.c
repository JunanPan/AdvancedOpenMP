#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "immintrin.h"
#include "kernel.h"
#include "omp.h"



//timing routine for reading the time stamp counter
static __inline__ unsigned long long rdtsc(void) {
  unsigned hi, lo;
  __asm__ __volatile__ ("rdtsc" : "=a"(lo), "=d"(hi));
  return ( (unsigned long long)lo)|( ((unsigned long long)hi)<<32 );
}

int main()
{

  double *a, *b, *c;
  int m = 8;
  int n = 6;
  int runs = 100;
  unsigned long long sum = 0;
  
  #pragma omp parallel num_threads(4)
  {
    
  unsigned long long sum = 0;
    unsigned long long t0, t1;  

    for (int k = 32; k <= 256; k += 32)
      {
         #pragma omp single
	  {
	    posix_memalign((void**) &a, 64, m * k * 4 * sizeof(double));
	    posix_memalign((void**) &b, 64, n * k * 4 * sizeof(double));
	    posix_memalign((void**) &c, 64, m * n * 4 * sizeof(double));
	    
	  }
	  
	  double *a_local, *b_local, *c_local;
	  a_local = a + m * k;
	  b_local = b + n * k;
	  c_local = c + m * n;
  
	  //initialize A
	  for (int i = 0; i != k * m; ++i){
	    a_local[i] = ((double) rand())/ ((double) RAND_MAX);
	  }
	  //initialize B
	  for (int i = 0; i != k * n; ++i){
	    b_local[i] = ((double) rand())/ ((double) RAND_MAX);
	  }
	  //initialize C
	  for (int i = 0; i != m * n; ++i){
	    c_local[i] = 0.0;
	  }

	  #pragma omp barrier	  
	  t0 = rdtsc();
	  for (int r = 0; r < runs; ++r)
	    kernel(k, a_local, b_local, c_local);

          #pragma omp barrier
	  t1 = rdtsc();	  
	  #pragma omp single
	  {
             printf("%d: %f\n", k, ((double)(t1-t0))/runs);
	      
	     free(a);
	     free(b);
	     free(c);
	  }
	  
      }
  }
  
  return 0;
}
