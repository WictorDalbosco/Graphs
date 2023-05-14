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
def dfs(graph,node):
    visited=set()
    sorvedouro=[]
    pais,maes=getParents()
    dfsRec(graph,node,visited,sorvedouro)
    visited=list(visited)

    sorvedouro.sort()
    
    for no in sorvedouro:
        p=parentsOfNode(no,pais,maes)
        if (p[0] in visited) and (p[1] in visited):
            print(no)
    return sorvedouro

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
    
    
# Driver code       
if __name__=='__main__':

    # Leitura e inicialização do grafo
    graph=getListaAdjacencias(input())
    
    n=len(graph)
    vis=[False]*n
    dfs_vis=[False]*n


    sorvedouros=dfs(graph,1)