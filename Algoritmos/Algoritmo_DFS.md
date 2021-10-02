# ALGORITMO DE DEPTH FIRST SEARCH (DFS)

## Implementación en pseudocódigo

DFS(Grafo G, nodo_fuente s)

  n = tamaño de G 
 
  visited = False
 
  parent = NULL 
 
  stack = [s] 
 
  Mientras stack no esté vacío hacer
 
   u = extraer_primero(stack)
   
     Si visited[u] es falso hacer
     
       visited[u] = verdadero
     
       Por cada v en G[u] hacer
       
         Si visited[v] es falso hacer
         
           parent[v] = u
           
           colocar al final de stack v 
           
           

## Posible orden de complejidad

La complejidad de un dfs puede expresarse como:

        O(|V| + |E|)

Donde:

        |V| es el número de nodos
        
        |E| es el número de aristas


El peor caso consistiría en que la solución a encontrar este en las últimas posiciones en cuanto a la profundidad o en los nodos siguientes que contengan otra profundidad, lo cual provocaría un tiempo de ejecución muy elevado.
  
