# Wictor Dalbosco Nº usp 11871027

class Grafo:

    #Inicializa o grafo
    def __init__(self, nVerticesGrafo):
 
        self.nVerticesGrafo = nVerticesGrafo
 
        # Ponteiro para vetor contendo lista de adjacência
        self.adj = [[] for i in range(1, self.nVerticesGrafo+1)]
 
    # Função que retorna o número de componetnes conectados de um grafo não dirigido     
    def DFS(self, v, visitados):
        
        global nVerticesConectados
        global posicao
        nVerticesConectados[posicao] += 1

        #Vetor de posições visitadas
        visitados[v] = True
        
        for i in self.adj[v]:
            if (not visitados[i]):
                self.DFS(i, visitados)
                  
    def calculaNumeroDeComponentesConectados(self):

        # Marca todos os vértices como não visitados
        visitados = [False for i in range(self.nVerticesGrafo)]

        global nVerticesConectados

        # Contador para componentes conectados
        contador = 0
        global posicao

        for v in range(self.nVerticesGrafo):
            if (visitados[v] == False):
              
                self.DFS(v, visitados)
                if (nVerticesConectados[posicao] > 2):
                    posicao +=1

                contador += 1
                
        return contador
    
    # Adiciona uma aresta no grafo
    def addVertice(self, v, w):
         
        self.adj[v].append(w)
        self.adj[w].append(v)

    # Lê um arquivo Pajek e retorna a lista de adjacências
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
    
    #Criamos um vetor global quer nos mostrará quantos vertices tem em cada grupo conectado
    global nVerticesConectados
    nVerticesConectados = [-1,0,0,0]

    posicao = 0

    #Recebemos quantos grupos temos        
    nComponentes = grafo.calculaNumeroDeComponentesConectados()
    nComponentes -= 1
    
    print(nComponentes)
    
    #Ordenamos em ordem descrescente
    nVerticesConectados.sort(reverse=True)
    
    for i in range(nComponentes):
        print(nVerticesConectados[i])