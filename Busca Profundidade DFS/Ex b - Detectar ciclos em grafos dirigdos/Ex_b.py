# Wictor Dalbosco Nº usp 11871027

class Grafo:

    #Inicializa o grafo
    def __init__(self, nVerticesGrafo):
 
        self.nVerticesGrafo = nVerticesGrafo
 
        # Ponteiro para vetor contendo lista de adjacência
        self.adj = [[] for i in range(1, self.nVerticesGrafo+1)]
 
    
    def DFS(self, v, visitado, pilhaRecursao):
 
        # Marca o nó atual como visitado
        visitado[v] = True
        
        # Adiciona a pilha de recursão
        pilhaRecursao[v] = True
 
        
        # Passando pelos vizinhos
        # Se um deles que for visitado estiver na pilha de recursão, entao o grafo é cíclico
        for vizinho in self.adj[v]:
            if visitado[vizinho] == False:
                if self.DFS(vizinho, visitado, pilhaRecursao) == True:
                    return True
            elif pilhaRecursao[vizinho] == True:
                return True
 
        #Desempilhando 
        pilhaRecursao[v] = False
        return False
 
    # Define se um dado grafo é cíclico ou não
    def isCyclic(self):
        visitado = [False] * (self.nVerticesGrafo + 1)
        pilhaRecursao = [False] * (self.nVerticesGrafo + 1)
        
        for node in range(self.nVerticesGrafo):
            if visitado[node] == False:
                if self.DFS(node,visitado,pilhaRecursao) == True:
                    return True

        return False
    
    # Adiciona uma aresta no grafo dirigido
    def addVertice(self, v, w):
        self.adj[v].append(w)

    # Lê um arquivo Pajek e retorna a lista de adjacências como dicionário
    def lerPajek(self,nomeArquivo):

        try:

            # Abre o arquivo
            with open(nomeArquivo, "r") as pajek:
                
                # Le quantidade de vertices e os recebe
                vertices = int(pajek.readline().split()[1])
                linhas = pajek.readlines()[1:]

                #Cria grafo
                grafo = Grafo(vertices+1)

                # Percorre os vertices
                for linha in linhas:
                    if(linha != "\n"):
                        comps = linha.split()
                        primeiroVertice = int(comps[0])
                        segundoVertice = int(comps[1])
                        grafo.addVertice(primeiroVertice,segundoVertice)

        except FileNotFoundError:
            print("Arquivo não encontrado!")
            exit(0)

        return grafo   
         
# Driver code       
if __name__=='__main__':
     
    #Inicializamos o grafo e lemos o pajek
    grafo = Grafo(0)
    grafo = grafo.lerPajek(input())

    if (grafo.isCyclic() == 1):
      print("S")
    else: 
      print("N")
    
    