run_small:
	gcc -O2 triangle.c -o triangle.x -std=c99 -DN=6474 -DNUM_A=25144 -fopenmp
	cat small_IA.txt small_JA.txt | OMP_NUM_THREADS=1 ./triangle.x 10
	cat small_IA.txt small_JA.txt | OMP_NUM_THREADS=2 ./triangle.x 10
	cat small_IA.txt small_JA.txt | OMP_NUM_THREADS=4 ./triangle.x 10
	cat small_IA.txt small_JA.txt | OMP_NUM_THREADS=8 ./triangle.x 10
	cat small_IA.txt small_JA.txt | OMP_NUM_THREADS=16 ./triangle.x 10
	cat small_IA.txt small_JA.txt | OMP_NUM_THREADS=32 ./triangle.x 10

run_medium:
	gcc -O2 triangle.c -o triangle.x -std=c99 -DN=9877 -DNUM_A=51946 -fopenmp
	cat medium_IA.txt medium_JA.txt | OMP_NUM_THREADS=1 ./triangle.x 10
	cat medium_IA.txt medium_JA.txt | OMP_NUM_THREADS=2 ./triangle.x 10
	cat medium_IA.txt medium_JA.txt | OMP_NUM_THREADS=4 ./triangle.x 10
	cat medium_IA.txt medium_JA.txt | OMP_NUM_THREADS=8 ./triangle.x 10
	cat medium_IA.txt medium_JA.txt | OMP_NUM_THREADS=16 ./triangle.x 10
	cat medium_IA.txt medium_JA.txt | OMP_NUM_THREADS=32 ./triangle.x 10

run_large:
	gcc -O2 triangle.c -o triangle.x -std=c99 -DN=22687 -DNUM_A=109410 -fopenmp
	cat large_IA.txt large_JA.txt | OMP_NUM_THREADS=1 ./triangle.x 10
	cat large_IA.txt large_JA.txt | OMP_NUM_THREADS=2 ./triangle.x 10
	cat large_IA.txt large_JA.txt | OMP_NUM_THREADS=4 ./triangle.x 10
	cat large_IA.txt large_JA.txt | OMP_NUM_THREADS=8 ./triangle.x 10
	cat large_IA.txt large_JA.txt | OMP_NUM_THREADS=16 ./triangle.x 10
	cat large_IA.txt large_JA.txt | OMP_NUM_THREADS=32 ./triangle.x 10

cleanup:
	rm -rf *~
	rm -rf *.x

