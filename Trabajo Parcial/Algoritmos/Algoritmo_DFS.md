# ALGORITMO DE DEPTH FIRST SEARCH (DFS)

## Concepto

El algoritmo de DFS se va aplicar para organizar y para trazar un camino desde los almacenes hacia los puntos de distribucion que estaran presentes en el mapeado de ellos, su fin es la de resolver eficientemente el problema a traves de la ejecucion del algoritmo. 

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

La complejidad de DFS:

        O(|V| + |E|)

Donde:

        |V| es el número de nodos
        
        |E| es el número de aristas


El peor caso consistiría en que la solución a encontrar esté en las últimas posiciones en cuanto a la profundidad o en los nodos siguientes que contengan otra profundidad, lo cual provocaría un tiempo de ejecución más elevado.
