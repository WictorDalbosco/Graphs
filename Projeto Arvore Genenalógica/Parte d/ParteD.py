# Jônatas Alves Lopes  N° USP 11796552
# Wictor Dalbosco      Nº USP 11871027
 
#  Método de leitura do pajek para grafos dirigidos
def getListaAdjacencias(nome_file):
    f = open(nome_file, "r")

    lines=[]

    i=0
    for line in f:
        i+=1
        lines.append(line)
    vertices=[]
    num_vertices=int(lines[0][10:])

    for i in range(num_vertices):
        vertices.append([])
        vertices[i].append(i+1)

    for i in range(2,len(lines)):
        if len(lines[i])>2:
            v1=lines[i].split("    ")[0]
            v2=lines[i].split("    ")[1]
            if not int(v2) in vertices[int(v1)-1]:
                vertices[int(v1)-1].append(int(v2))
    return vertices

# Método para contar as fontes do grafo dirigido
def printNumberOfSources(graph):
    
    count=[0]*len(graph)
    for no in graph:
        for i in range(1,len(no)):
            count[no[i]-1]+=1
            
    numSources=0
    for n in count:
        if n==0:
            numSources+=1
    print(numSources)

# Método para contar os sorvedouros do grafo dirigido
def printNumberOfSorvedouro(graph):
    numSorvedouro=0
    for no in graph:
        if(len(no)==1):
            numSorvedouro+=1
    print(numSorvedouro)

# Método auxiliar recursivo para a DFS
def dfsRec(g,node,vis,s):
    vis.add(node)
    if len(g[node-1])==1:
       s.append(node)

    for adjNode in g[node-1]:
        if adjNode not in vis:
            dfsRec(g,adjNode,vis,s)

# Método para a DFS dado um grafo e um nó
def getSorvedouros(graph,node,pais,maes):
    visited=set()
    sorvedouro=[]
    dfsRec(graph,node,visited,sorvedouro)
    visited=list(visited)

    sorvedouro.sort()
    sorvAmbosPais=[]
    for no in sorvedouro:
        p=parentsOfNode(no,pais,maes)
        if (p[0] in visited) and (p[1] in visited):
            sorvAmbosPais.append(no)
    return sorvAmbosPais

# Método para recuperar os pais de todos os nó 
def getParents():
    pai=[-1]*n
    mae=[0-1]*n
    qtdPais=[0]*n

    for no in graph:
        for i in range(1,len(no)):
            filho=no[i]
            if pai[filho-1]==-1:
                pai[filho-1]=no[0]
            else:
                mae[filho-1]=no[0]
            qtdPais[filho-1]+=1

    return pai, mae

# Método para retornar os pais de dado um nó
def parentsOfNode(node,pais,maes):
    parents=[]
    parents.append(pais[node-1])
    parents.append(maes[node-1])

    return parents
    
#Metodo para realizar bfs em um grafo
def bfs(visited, graph,node,queue,pai):
    visited.append(node)
    queue.append(node)

    # Creating loop to visit each node
    while queue:         
        m = queue.pop(0) 

        for neighbour in graph[m-1]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                pai[neighbour-1]=m

# Método para reconstruir um caminho de um nó
def reconstructPath(e,prev):
  path=[]
  at=e-1
  while(at!=-1):
    at=prev[at]
    if(at!=-1):
        path.append(at)
        at-=1
  return path

# Método para retornar o pai do nó
def linhagemDoNo(graph, node):
    visited = [] # List for visited nodes.
    queue = []   #Initialize a queue
    pai=[-1]*n
    bfs(visited,graph,node,queue,pai)
    return pai

# Método para retornar a distância do vértice 1
def distanciaAteUm(no, linhagem):
    return len(reconstructPath(no,linhagem))

# Método para realizar a soma mínima
def somaMinima(graph,pais,maes):

    linhagem=linhagemDoNo(graph,1)
    soma=[]

    for no in sorv:
        p=parentsOfNode(no,pais,maes)
        somaDist=distanciaAteUm(p[0],linhagem)+distanciaAteUm(p[1],linhagem)
        soma.append((somaDist,no))
        soma.sort(key=lambda tup: tup[0])
        
    for no in soma:
        if(no[0]==soma[0][0]):
            print(no[1])
    

# Driver code       
if __name__=='__main__':

    # Leitura e inicialização do grafo
    graph=getListaAdjacencias(input())
    
    n=len(graph)
    vis=[False]*n
    dfs_vis=[False]*n

    pais,maes=getParents()
    sorv= getSorvedouros(graph,1,pais,maes)
    
    somaMinima(graph,pais,maes)
    