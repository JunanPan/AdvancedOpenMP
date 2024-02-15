all:
	gcc -O2 affinity.c -o affinity.x -std=c99 -mfma -mavx -fopenmp 
	./affinity.x

run:
	./affinity.x

clean:
	rm -rf *~ *.x
