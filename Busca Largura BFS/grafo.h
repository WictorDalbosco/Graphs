#ifndef _grafo_

#define _grafo_

#include <stdio.h>
#include <stdlib.h>

//Estruturar grafo
struct No* criaNo(int v);
struct Grafo* criaGrafo(int vertices);
void adicionaVertice(struct Grafo* grafo, int src, int dest);
void printaMatrizAdj(struct Grafo* grafo); 
void liberarGrafo(struct Grafo *grafo);

//Fila para a bfs
struct fila* criarFila();
void enfileirar(struct fila* f, int);
int desenfileirar(struct fila* f);
void mostrar(struct fila* f);
int estaVazia(struct fila* f);
void printFila(struct fila* f);

//BFS
void bfs(struct Grafo* grafo, int verticeInicial, int verticeFinal);


#endif


