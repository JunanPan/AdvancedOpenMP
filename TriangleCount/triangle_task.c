#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include "rdtsc.h"

unsigned int *IA;
unsigned int *JA;


void input() {
    unsigned int num_IA = N + 1;
    unsigned int num_JA = NUM_A;    
    
    IA = (unsigned int*)malloc((N+1) * sizeof(unsigned int));
    JA = (unsigned int*)malloc(NUM_A * sizeof(unsigned int));    
    
    for(unsigned int i = 0; i<num_IA; i++) scanf("%d", &IA[i]);
    for(unsigned int i = 0; i<num_JA; i++) scanf("%d", &JA[i]);
}

unsigned int count_triangles() {
  unsigned int delta = 0; 

  #pragma omp parallel
  {
    #pragma omp single
    {
      // The outer loop traverses over all possible vertices (y). The iteration starts with vertex #1
      for(unsigned int i = 1; i<N-1; i++) {                    
        #pragma omp task firstprivate(i) shared(IA, JA) reduction(+:delta)
        {
          unsigned int *curr_row_x = IA+i;
          unsigned int *curr_row_A = IA+i+1;
          unsigned int num_nnz_curr_row_x = *curr_row_A - *curr_row_x;
          unsigned int *x_col_begin = (JA + *curr_row_x);
          unsigned int *x_col_end = x_col_begin;
          unsigned int *row_bound = x_col_begin + num_nnz_curr_row_x;
          unsigned int col_x_min = 0;
          unsigned int col_x_max = i-1;
          
          while(x_col_end < row_bound && *x_col_end < col_x_max) ++x_col_end;
          x_col_end -= (*x_col_end > col_x_max || x_col_end == row_bound);
              
          unsigned int *y_col_begin = x_col_end + 1;
          unsigned int *y_col_end = row_bound-1;
          unsigned int num_nnz_y = (y_col_end - y_col_begin) + 1;
          unsigned int num_nnz_x = (x_col_end - x_col_begin) + 1;
              
          unsigned int y_col_first = i + 1;
          unsigned int x_col_first = 0;
          unsigned int *y_col = y_col_begin;

          // This is where the real triangle counting begins.
          // We search through all possible vertices for x
          for(unsigned int j = 0; j < num_nnz_y; ++j,++y_col) {
            unsigned int row_index_A = *y_col - y_col_first;             
            unsigned int *x_col = x_col_begin;           
            unsigned int num_nnz_A = *(curr_row_A + row_index_A + 1) - *(curr_row_A + row_index_A);
            unsigned int *A_col = (JA + *(curr_row_A + row_index_A));           
            unsigned int *A_col_max = A_col + num_nnz_A;
            
            // This loop searches through all possible vertices for z.
            for(unsigned int k = 0; k < num_nnz_x && *A_col <= col_x_max; ++k) {                
              unsigned int row_index_x = *x_col - x_col_first;               
              while((*A_col < *x_col) && (A_col < A_col_max)) ++A_col;

              // A triangle is found if the condition returns true
              delta += (*A_col == row_index_x);
              
              ++x_col;               
            }       
          }
        }
      }
    }
    #pragma omp taskwait
  }
  
  return delta;
}


int main(int argc, char **argv) {
    int runs = atoi(argv[1]);

    tsc_counter t0, t1;

    input();

    long long sum1 = 0;
    
    for(unsigned int i = 0; i != runs; ++i) {
        unsigned int x = 0;
        
        RDTSC(t0);
        x = count_triangles();
        RDTSC(t1);
        // printf("%u\n", x);
        sum1 += (COUNTER_DIFF(t1, t0, CYCLES));
    }
    
    free(IA);
    free(JA);
    
    printf("Average Triangle Count time: %lf cycles\n", ((double) (sum1 / ((double) runs))));
    return 0;
}
