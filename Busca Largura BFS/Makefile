Codigos =  BFS.c grafo.c

all:
	@gcc $(Codigos) -o bfs -lm -Wall -Werror

run:
	@./bfs

valgrind:
	@valgrind --track-origins=yes --leak-check=full --show-leak-kinds=all ./bfs 

zip:
	zip -r bfs.zip Makefile ./bfs.c 