# Impletación en pseudocódigo

    BFS(Grafo G, nodo_fuente s)
    n = tamaño de G 
    parent = NULL
    visited = False
    queue = [s]
    visited[s] = True

    Mientras queue no esté vacío hacer
      u = extraer_primero(queue)
      Por cada v en G[u] hacer
        Si visited[v] es falso hacer
          visited[v] = verdadero
          parent[v] = u
          colocar al final de queue v 


# Posible orden de complejidad
La complejidad de un bfs puede expresarse como:

<img src="https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_white&space;O(|V|&plus;|E|)" title="\bg_white O(|V|+|E|)" />

$$f\left(k\right) = \binom{n}{k} p^k\left(1-p\right)^{n-k}$$ 

Donde: 

|V| es el número de nodos

|E| es el número de aristas


**El peor caso consistiría en que todos los nodos y aristas sean visitados durante la búsqueda.**
