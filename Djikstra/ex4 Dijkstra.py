# Wictor Dalbosco Nº usp 11871027

import numpy as np
from enum import Enum

class Cor(Enum):
    BRANCO = 1
    PRETO = 2
    CINZA = 3

class NodeEdge:

    def __init__(self, vertice, peso):
        self.vertice = vertice
        self.peso = peso

class NoV:

    def __init__(self, vertice, cor):
        self.vertice = vertice
        self.cor = cor
        self.listaAdj = []
        self.distancia = np.inf

class Graph:
    
    #Inicialização da leitura do arquivo Pajek
    def __init__(self, nomeArquivoPajek):

        self.vertices = []
        self.nVertices = 0
        self.matriz = [[] for i in range(1, self.nVertices+1)]

        #Formatação de string
        def __str__(self):
            string = ""

            for i in range(0, self.nVertices):
                string = string + "vertice:"+str(i+1) + "\n"
                for edge in self.vertices[i].listaAdj:
                    string = string + "  |-> "+str(edge.vertice+1)+"  "+str(edge.peso)
                    string = string + "\n"

            
            return string

        #Leitura de vertices de um grafo não dirigido
        def leVertice(string):
            for linha in string:
                dadosVertice = linha.split()
                if (len(dadosVertice) < 3):
                    peso = 1
                else:
                    peso = int(dadosVertice[2])

                self.inserirVertice(int(dadosVertice[0])-1, int(dadosVertice[1])-1, peso)
                self.inserirVertice(int(dadosVertice[1])-1, int(dadosVertice[0])-1, peso)

        #Leitura de vertices de um grafo não dirigido
        def leArco(string):
            for linha in string:
                dadosVertice = linha.split()
                if (len(dadosVertice) < 3):
                    peso = 1
                else:
                    peso = int(dadosVertice[2])

                self.inserirVertice(int(dadosVertice[0])-1, int(dadosVertice[1])-1, peso)

        try:

            #Leitura do arquivo pajek
            with open(nomeArquivoPajek, "r") as pajek:
                string = pajek.readlines()

                #Lendo o número de vértices
                linha = string[0].split()
                self.nVertices = int(linha[1])

                #Anotando todos os vértices como não visitados (BRANCO)
                for i in range (self.nVertices):
                    n = NoV(i, Cor.BRANCO)
                    self.vertices.append(n)

                linha = string[1]

                #Divisão de leitura caso seja um grafo dirigido ou não dirigido 
                if("Edges" in linha):
                    leVertice(string[2:])
                elif("Arcs" in linha):
                    leArco(string[2:])

        except FileNotFoundError:
            print("Arquivo não encontrado!")
            exit(0)

    #Funcionalidade de inserção de vértices
    def inserirVertice(self, gSrc, gDest, peso):

        newEdge = NodeEdge(gDest, peso) 
        self.vertices[gSrc].listaAdj.append(newEdge)
        return
    #Algoritmo de busca de Dijkstra para um vértice
    def dijkstra(self, indiceInicio):

        L_Brancos = []
        for i in range(0, self.nVertices):
            self.vertices[i].cor = Cor.BRANCO
            self.vertices[i].distancia = np.inf
            L_Brancos.append(self.vertices[i])

        indiceAtual = indiceInicio
        self.vertices[indiceAtual].distancia = 0

        while(len(L_Brancos) > 0):

            L_Brancos = sorted(L_Brancos, key=lambda vertice: vertice.distancia)
            cur_vertex = L_Brancos[0]

            for node in cur_vertex.listaAdj:
                node_vertex = self.vertices[node.vertice]
                cur_distance = cur_vertex.distancia + node.peso

                if (node_vertex.cor == Cor.BRANCO and cur_distance < node_vertex.distancia):
                    node_vertex.distancia = cur_distance
                
            if (cur_vertex.cor == Cor.BRANCO):
                L_Brancos.remove(cur_vertex)
                cur_vertex.cor = Cor.PRETO

        vetorDistancias = []

        for vertice in self.vertices:
            vetorDistancias.append(vertice.distancia)
        
        self.matriz.append(vetorDistancias)

# Driver code       
if __name__=='__main__':

    #Cria um grafo a partir de um arquivo pajek de entrada
    grafo = Graph(input())

    #Realiza a busca através do algoritmo de Dijkstra
    for i in range(0, grafo.nVertices):
        grafo.dijkstra(i)
    
    #Auxílio no padding da matriz
    aux = len(str(max(max(grafo.matriz))))

    #Impressão da matriz formatada de distancias
    for linha in (grafo.matriz):
        for dist in linha:
            print(f'{dist:>{aux}}', end=' ')
        print()
