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

# Driver code       
if __name__=='__main__':

    # Leitura e inicialização do grafo
    graph=getListaAdjacencias(input())

    printNumberOfSources(graph)

