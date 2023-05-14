// BFS algorithm in C

#include <stdio.h>
#include <stdlib.h>
#include "grafo.h"

int main(){
  struct Grafo* grafo = criaGrafo(6);

  adicionaVertice(grafo, 1, 2);
  adicionaVertice(grafo, 1, 3);
  adicionaVertice(grafo, 1, 4);
  adicionaVertice(grafo, 4, 5);

  printf("Ponto 2\n");
  bfs(grafo, 1,2);
  

  //liberarGrafo(grafo);

  //printaMatrizAdj(grafo);

  return 0;
}