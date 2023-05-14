#include <stdio.h>
#include <stdlib.h>
#include "grafo.h"
#define SIZE 40


struct No {
  int vertice;
  struct No* proximo;
};

struct Grafo {
  int numVertices;
  struct No** listasAdj;
  int *visitado;
};

struct fila {
  int items[SIZE];
  int frente;
  int tras;
};

// Função de busca em largura
void bfs(struct Grafo* grafo, int verticeInicial,int verticeFinal) {
  struct fila* f = criarFila();
  int distancia[grafo->numVertices];

  distancia[verticeInicial] = 0;

  grafo->visitado[verticeInicial] = 1;
  enfileirar(f, verticeInicial);

  while (!estaVazia(f)) {
    printFila(f);
    int q = f->frente;
    int verticeAtual = desenfileirar(f);
    printf("\nVisitado %d\n", verticeAtual);
    if (verticeAtual == verticeFinal){
      printf("Distancia entre %d e %d é %d\n",verticeInicial,verticeFinal,distancia);
      break;
    }
    
    /*for (int i = 0; i < grafo->numVertices; i++)
    {
      if(grafo->visitado[grafo->listasAdj[q][i]]){
        continue;
      }

      distancia[grafo->listasAdj[q][i]] = distancia[q]+1;
      enfileirar(f,verticeAdj)
    }*/
    


    struct No* temp = grafo->listasAdj[verticeAtual];

    while (temp) {
      int verticeAdj = temp->vertice;

      if (grafo->visitado[verticeAdj] == 0) {
        grafo->visitado[verticeAdj] = 1;
        enfileirar(f, verticeAdj);
        
      }
      temp = temp->proximo;
    }
  }
}

// Cria uma fila
struct fila* criarFila() {
  struct fila* f = malloc(sizeof(struct fila));
  f->frente = -1;
  f->tras = -1;
  return f;
}

// Checar se fila esta vazia
int estaVazia(struct fila* f) {
  if (f->tras == -1)
    return 1;
  else
    return 0;
}

// Adicionando elementos na fila
void enfileirar(struct fila* f, int valor) {
  if (f->tras == SIZE - 1)
    printf("\nFila cheia!!");
  else{
    if (f->frente == -1)
      f->frente = 0;
    f->tras++;
    f->items[f->tras] = valor;
  }
}

// Removing elements from fila
int desenfileirar(struct fila* f) {
  int item;
  if (estaVazia(f)) {
    printf("Fila vazia\n");
    item = -1;
  } else {
    item = f->items[f->frente];
    f->frente++;
    if (f->frente > f->tras) {
      //printf("\nFila restaurada\n");
      f->frente = f->tras = -1;
    }
  }
  return item;
}

// Print the fila
void printFila(struct fila* f) {
  int i = f->frente;

  if (estaVazia(f)) {
    printf("Fila vazia");
  } else {
    printf("\nFila contem ");
    for (i = f->frente; i < f->tras + 1; i++) {
      printf("%d ", f->items[i]);
    }
  }
}
// Criando um No
struct No* criaNo(int v) {
  struct No* novoNo = malloc(sizeof(struct No));
  novoNo->vertice = v;
  novoNo->proximo = NULL;
  return novoNo;
}

// Criando um grafo
struct Grafo* criaGrafo(int vertices) {
  struct Grafo* grafo = malloc(sizeof(struct Grafo));
  grafo->numVertices = vertices;

  grafo->listasAdj = malloc(vertices * sizeof(struct No*));
  grafo->visitado = malloc(vertices * sizeof(int));

  int i;
  for (i = 0; i < vertices; i++) {
    grafo->listasAdj[i] = NULL;
    grafo->visitado[i] = 0;
  }

  return grafo;
}

// Adiciona vertice
void adicionaVertice(struct Grafo* grafo, int src, int dest) {
  // Adiciona vertice da src para o dest
  struct No* novoNo = criaNo(dest);
  novoNo->proximo = grafo->listasAdj[src];
  grafo->listasAdj[src] = novoNo;

  // Adiciona vertice do dest para a src
  novoNo = criaNo(src);
  novoNo->proximo = grafo->listasAdj[dest];
  grafo->listasAdj[dest] = novoNo;
}

// Printar a matriz
void printaMatrizAdj(struct Grafo* grafo) {

  for (int i = 0; i < grafo->numVertices; i++) {
    printf("%d: ", i);
    for (int j = 0; j < grafo->numVertices; j++) {
      printf("%d ", grafo->listasAdj[i]->vertice);
    }
    printf("\n");
  }
}

void liberarGrafo(struct Grafo *grafo){
    struct No *aux;
    struct No *aux2;
    
    for (int i=0; i< grafo->numVertices; i++){
        if (grafo[i].listasAdj != NULL){
            aux = grafo[i].listasAdj[i];
            while (aux != NULL){
                aux2 = aux;
                aux = aux->proximo;
                free(aux2);
            }
            grafo->listasAdj = NULL;
        }
    }

    free(grafo);
    return;
}