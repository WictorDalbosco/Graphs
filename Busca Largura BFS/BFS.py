# Lê um arquivo Pajek e retorna a lista de adjacências como dicionário
def lerPajek(nomeArquivo):

    # Cria um dicionario de listas
    listaAdjacencia = {}

    try:

        # Abre o arquivo
        with open(nomeArquivo, "r") as pajek:
            
            # Le quantidade de vertices e os recebe
            vertices = int(pajek.readline().split()[1])
            linhas = pajek.readlines()[1:]

            # Inicializa os vertices
            for i in range(1, vertices+1):
                listaAdjacencia[i] = []

            # Percorre os vertices
            for linha in linhas:
                comps = linha.split()
                primeiroVertice = int(comps[0])
                segundoVertice = int(comps[1])

                listaAdjacencia[primeiroVertice].append(segundoVertice)
                listaAdjacencia[segundoVertice].append(primeiroVertice)

    except FileNotFoundError:
        print("Arquivo não encontrado!")
        exit(0)

    return [listaAdjacencia,vertices]

#Imprime uma lista de ajacencia
def print_listaAdjacencia(listaAdjacencia):
    for vertice in listaAdjacencia:
        print(str(vertice) + ": " + str(listaAdjacencia[vertice]))

#Função que realiza uma BFS
def BFS(lista, verticeIncial):
    
    #Vetores utilizadas para a BFS
    fila = []
    distancias = []
    verticesVisitados = []

    #Inicializa lista de vertices coloridos e de distancia
    for i in range(len(lista)+1):
        verticesVisitados.append(0)
        distancias.append(-1)

    fila.append(verticeIncial)
    distancias[verticeIncial] = 0
    verticesVisitados[verticeIncial] = 1

    #Navega pela fila, criando vetor de distancias
    while(len(fila) > 0):
        verticeAtual = fila.pop(0)

        for i in range(len(lista[verticeAtual])):

            verticeLista = lista[verticeAtual][i]

            if(verticesVisitados[verticeLista] == 0):
                verticesVisitados[verticeLista] = 1
                fila.append(verticeLista)
                distancias[verticeLista] = distancias[verticeAtual]+1

    return distancias

#Função que printa uma matrizDistancia quadrada começando do indice 1    
def printMatrizDist(matrizDistancia):
    for i in range(1, len(matrizDistancia)):
        linha = ""
        for j in range(1, len(matrizDistancia)):
            linha = linha + str(matrizDistancia[i][j]) + " "
        print(linha)

#Construir uma matriz de distancias
def montaMatrizDistancia(lista, vertices):
    matrizDistancia = []
     
    #Inicializa a matriz
    for i in range(vertices+1):
        matrizDistancia.append([])
        for j in range(vertices+1):
            matrizDistancia[i].append(0)

    
    for i in range(1, vertices+1):
        
        #Monta vetor de distancias a partir de uma bfs
        distancias = BFS(lista, i)

        for j in range(i+1, vertices+1):
            matrizDistancia[i][j] = distancias[j]
            matrizDistancia[j][i] = distancias[j]

    return matrizDistancia


# Main ####################################################

# Ler o Pajek
listaAdjacencia,vertices = lerPajek(input())

# Exibe a lista original
#print("Lista de ajacência a partir do pajek:")
#print_listaAdjacencia(listaAdjacencia)

matrizDistancias = montaMatrizDistancia(listaAdjacencia,vertices)

#print("Matriz de distâncias: ")
printMatrizDist(matrizDistancias)

