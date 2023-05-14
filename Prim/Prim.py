# Wictor Dalbosco Nº usp 11871027

from enum import Enum
import numpy as np

class ArestaNo:

    def __init__(self, vertice, peso):
        self.vertice = vertice
        self.peso = peso

class NoV:

    def __init__(self, vertice, cor):
        self.vertice = vertice
        self.cor = cor
        self.listaAdj = []
        self.distancia = np.inf

class Grafo:

    def __init__(self, filename):

        self.vertices = []
        self.nVertices = 0

        #Lê edges para grafos não dirigidos
        def leEdges(string):
            for linha in string:
                dadoVertice = linha.split()
                if (len(dadoVertice) < 3):
                    peso = 1
                else:
                    peso = int(dadoVertice[2])
                self.insereVertice(int(dadoVertice[0])-1, int(dadoVertice[1])-1, peso)
                self.insereVertice(int(dadoVertice[1])-1, int(dadoVertice[0])-1, peso)

        #Le arcos, ou seja, grafos dirigdos
        def leArco(string):
            for linha in string:
                dadoVertice = linha.split()
                if (len(dadoVertice) < 3):
                    peso = 1
                else:
                    peso = int(dadoVertice[2])
                self.insereVertice(int(dadoVertice[0])-1, int(dadoVertice[1])-1, peso)

        #Leitura do pajek
        with open(filename, "r") as pajek:
            string = pajek.readlines()

            #Leitura do número de vértices
            linha = string[0].split()
            self.nVertices = int(linha[1])

            #Inicializa todos como vértices Brancos
            for i in range (self.nVertices):
                n = NoV(i, 'B')
                self.vertices.append(n)

            linha = string[1]
            if("Edges" in linha):
                leEdges(string[2:])
            elif("Arcs" in linha):
                leArco(string[2:])

    #Método para formatação de strings
    def __str__(self):
        string = ""

        for i in range(0, self.nVertices):
            string = string + "vertice:"+str(i+1) + "\n"
            for edge in self.vertices[i].listaAdj:
                string = string + "  |-> "+str(edge.vertice+1)+"  "+str(edge.peso)
                string = string + "\n"

        return string

    #Método para inserir um vértice de forma a checar se um vértice de destino ja tem uma aresta com vértice gSrc
    def insereVertice(self, gSrc, gDest, peso):

        newEdge = ArestaNo(gDest, peso) 
        self.vertices[gSrc].listaAdj.append(newEdge)
        return

    #Algoritmo de Prim para encontrar a soma da árvore geradora mínima de um grafo
    def prim(self):

        L_Branco = []
        L_Preto = []
        for i in range(0, self.nVertices):
            self.vertices[i].cor = 'B'
            self.vertices[i].distancia = np.inf
            L_Branco.append(self.vertices[i])

        #Inicializa com 0 o índice
        indiceAtual = 0
        self.vertices[indiceAtual].distancia = 0

        somaDistancia = 0
        while(len(L_Branco) > 0):

            #Ordena L_Branco de acordo com a menor distância
            L_Branco = sorted(L_Branco, key=lambda vertice: vertice.distancia)
            verticeAtual = L_Branco[0]

            for no in verticeAtual.listaAdj:
                node_vertex = self.vertices[no.vertice]

                if (node_vertex.cor == 'B' and no.peso < node_vertex.distancia):
                    node_vertex.distancia = no.peso
                
            if (verticeAtual.cor == 'B'):
                L_Branco.remove(verticeAtual)
                verticeAtual.cor = 'P'
                L_Preto.append(verticeAtual)
                somaDistancia += verticeAtual.distancia

        print(somaDistancia)

# Driver code       
if __name__=='__main__':     
  
  grafo = Grafo(input())
  grafo.prim()