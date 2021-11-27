# CC41 - TRABAJO FINAL 2021 2
### Integrantes
  - Coronel Manchego, Gianella
  - Mollan Neyra, Klaus Matthew
  - Morante Castañeda, Augusto Gerardo
  - Roncal Mejía, José Luis
  - Villalobos Curichimba, Katerin
### Introducción
Para el presente trabajo se planteó el problema de enrutamiento de vehículos (VRP), con el objetivo de buscar un balance entre el tiempo y costo de entrega. Por ello, se debe buscar el conjunto de rutas óptimas para una flota de vehículos y de esa manera obtener la mayor satisfacción por parte de los clientes, lo cual nos ayudará a tener una mayor ganancia y así conseguir más clientes satisfechos. 
### Objetivos
  - Aplicar la competencia general de razonamiento cuantitativo.
### Marco Teorico
#### Algoritmo Dijkstra
El algoritmo de Dijkstra es una algoritmo para encontrar el camino más corto en un grafo. A diferencia de DFS, Dijkstra puede calcular el camino más corto en un grafos con pesos.
  - Utilizando cola de prioridad: O(|E|+|V|log⁡|V|)
  - Sin utilizar cola de prioridad: O(|V2|+E)
#### Algoritmo Breadth-First Search (BFS):
El algoritmo de BFS busca aplicar de forma eficiente y organizada y para trazar un camino desde los almacenes hacia los puntos de distribución que estarán presentes en el mapeado de ellos, su finalidad es explorar los todos nodos vecinos por cada nodo para encontrar el mejor camino. 
  - Su complejidad es: O(V+E)
#### Algoritmo Depth First Search (DFS):
El algoritmo de DFS se va aplicar para organizar y para trazar un camino desde los almacenes hacia los puntos de distribución que estarán presentes en el mapeado de ellos, su fin es la de resolver eficientemente el problema a través de la ejecución del algoritmo, puesto que hara una busqueda en profundidad según la cantidad de nodos que se encuentren debajo.
  - Su complejidad es: O(V+E)
#### Algoritmo Brute Force:
El algoritmo de fuerza bruta nos ayudará en el problema de enrutamiento propuesto, puesto que encontrará la ruta más corta entre el almacén y el punto de entrega. Por ello, tomaremos el nodo en la posición inicial y final para hallar la ruta mínima. De esta manera, poder encontrar la mejor solución y distancia entre cada punto.
  - Su complejidad es: O(n^2)
#### Algoritmo Backtracking:
El algoritmo de Backtracking, también conocido como Vuelta atrás, es un tipo de algoritmo de búsqueda en profundidad porque se dedica a hallar una adecuada combinación en determinado momento. Mientras hace su recorrido, si encuentra una solución incorrecta, regresa un paso para encontrar un mejor resultado.
  - Su complejidad es: O(a^n)
    - Donde:
    - a: Son las posibles opciones que hay en cada etapa.
    - n: Número de etapas que se toman para hallar la solución.
### Resultados
#### Solucion con Dijkstra
Para la solución del Dijkstra, se trabaja con los siguientes algoritmos:
~~~
def dijkstraPointToPoint(G, s, t):
  n = len(G)
  visited = [False]*n
  path = [None]*n
  cost = [math.inf]*n
  cost[s] = 0
  queue = [(0, s)]
  while queue and visited[t] == False:
    g_u, u = hq.heappop(queue)
    if not visited[u]:
      visited[u] = True
      for v, w in G[u]:
        f = g_u + w
        if f < cost[v]:
          cost[v] = f
          path[v] = u
          hq.heappush(queue, (f, v))

  return path, cost, visited, cost[t]
~~~
~~~
def dijkstraPointToPointOnlyCost(G, s, t):
  n = len(G)
  visited = [False]*n
  path = [None]*n
  cost = [math.inf]*n
  cost[s] = 0
  queue = [(0, s)]
  while queue and visited[t] == False:
    g_u, u = hq.heappop(queue)
    if not visited[u]:
      visited[u] = True
      for v, w in G[u]:
        f = g_u + w
        if f < cost[v]:
          cost[v] = f
          path[v] = u
          hq.heappush(queue, (f, v))

  return cost[t]
~~~
~~~
def showInfo(G, source, target):
  path, cost, _, _ = dijkstraPointToPoint(G, source, target)
  t = target
  targetPath = []
  targetPath.append(target)
  targetPath.append(path[t])
  while path[t] != source:
    t = path[t]
    targetPath.append(path[t])
    
  targetPath = list(reversed(targetPath)) 

  return targetPath, cost[target]
~~~
#### Solucion con BFS
Para la solución del BFS, se trabaja con los siguientes algoritmos:
~~~
def bfsPointToPoint(G, s, t):
  n = len(G)
  visited = [False]*n
  parent = [None]*n
  queue = [s]
  visited[s] = True

  while queue and visited[t] == False:
    u = queue.pop(0)
    for v in G[u]:
      if not visited[v]:
        visited[v] = True
        parent[v] = u
        queue.append(v)

  return parent, parent[t]
~~~
~~~
def showInfoBFS(G, source, target):
  path,_ = bfsPointToPoint(G, source, target)
  t = target
  targetPath = []
  targetPath.append(target)
  targetPath.append(path[t])
  while path[t] != source:
    t = path[t]
    targetPath.append(path[t])

  truePath = path
  for i in range(len(truePath)):
    if i not in targetPath and i != target:
      truePath[i] = None 

  return targetPath, truePath, len(targetPath)-1
~~~
~~~
def BFSPointToPointEdges(G, source, target):
  path,_ = bfsPointToPoint(G, source, target)
  t = target
  targetPath = []
  targetPath.append(target)
  targetPath.append(path[t])
  while path[t] != source:
    t = path[t]
    targetPath.append(path[t])
  return len(targetPath)-1
~~~
Almacenes analizados desde el 11 al 20:
  - De los almacenes analizados, el resultado más corto, el cual debe realizar un menor recorrido en cuestión de distancia fue el del almacén 17, con 14 entregas.
  - El tiempo de ejecución con respecto a ese almacén fue de 1.42327 ms.
  - El tiempo de ejecución promedio de los 10 almacenes fue de 5.03959 ms.
#### Solucion con DFS
Para la solución del DFS, se trabaja con los siguientes algoritmos:
~~~
def dfsPointToPoint(G, s, t):
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    stack = [s]

    while stack and visited[t] == False:
      u = stack.pop()
      if not visited[u]:
        visited[u] = True
        for v in G[u]:
          if not visited[v]:
            parent[v] = u
            stack.append(v)

    return parent, parent[t]
~~~
~~~
def showInfoDFS(G, source, target):
    path,_ = dfsPointToPoint(G, source, target)
    t = target
    targetPath = []
    targetPath.append(target)
    targetPath.append(path[t])
    while path[t] != source:
      t = path[t]
      targetPath.append(path[t])

    truePath = path
    for i in range(len(truePath)):
      if i not in targetPath and i != target:
        truePath[i] = None 

    return targetPath, truePath, len(targetPath)-1
~~~
~~~
def DFSPointToPointEdges(G, source, target):
  path,_ = dfsPointToPoint(G, source, target)
  t = target
  targetPath = []
  targetPath.append(target)
  targetPath.append(path[t])
  while path[t] != source:
    t = path[t]
    targetPath.append(path[t])
  return len(targetPath)-1
~~~
Almacenes analizados desde el 41 al 50:
  - De los almacenes analizados, el resultado más corto, el cual debe realizar un menor recorrido en cuestión de distancia fue el del almacén 45.
  - El tiempo de ejecución con respecto a ese almacén fue de 7865 ms.
  - El tiempo de ejecución promedio de los 10 almacenes fue de 19700 ms.
#### Solucion con Brute Force
Para la solución de Brute Force, se trabaja con los siguientes algoritmos:
~~~
def bruteforce(G, s):
  n = len(G)
  tvisit = [None, s]
  path = []
  visited = [False]*n
  while(tvisit):
    v = tvisit.pop()
    if v : 
      path.append(v)
      if len(path) == n:
        break
      visited[v]
      for x in G[v]:
        tvisit.append(None)
        tvisit.append(x) 
  return path
~~~
~~~
def bfPointToPoint(G,s,t):
  n = len(G)
  tvisit = [None, s]
  path = []
  visited = [False]*n
  while(tvisit):
    v = tvisit.pop()
    if v : 
      path.append(v)
      if len(path) == n:
        break
      visited[v]
      for x in G[v]:
        tvisit.append(None)
        tvisit.append(x) 
  return path, path[t]
~~~
~~~
def BFPointToPointEdges(G, source, target):
  path,_ = bfPointToPoint(G, source, target)
  t = target
  targetPath = []
  targetPath.append(target)
  targetPath.append(path[t])
  while path[t] != source:
    t = path[t]
    targetPath.append(path[t])
  return len(targetPath)-1
~~~
Almacenes analizados desde el 31 al 40:
  - De los almacenes analizados, el resultado más corto, el cual debe realizar un menor recorrido en cuestión de distancia fue el del almacén 37.
  - El tiempo de ejecución con respecto a ese almacén fue de 4462 ms.
  - El tiempo de ejecución promedio de los 10 almacenes fue de 25900 ms.
#### Solucion con Backtracking
Para la solución de Backtracking, se trabaja con los siguientes algoritmos:
~~~
def backtracking(G, s):
  n = len(G)
  visited = [False]*n
  parent = [None]*n
  
  def Backtracking1(e):
    visited[e] = True
    for v in G[e]:
      if not visited[v]:
        parent[v] = e
        Backtracking1(v)

  Backtracking1(s)

  return parent
~~~
~~~
def backtrackingPointToPoint(G, s, t):
  n = len(G)
  visited = [False]*n
  parent = [None]*n
  def Backtracking2(e, d):
    visited[e] = True
    for v in G[e]:
      if e != d and visited[d] == False:
        if not visited[v]:
          parent[v] = e
          Backtracking2(v, d)
      
  Backtracking2(s, t)

  return parent, parent[t]

def BacktrackingPointToPointEdges(G, source, target):
  path,_ = backtrackingPointToPoint(G, source, target)
  t = target
  targetPath = []
  targetPath.append(target)
  targetPath.append(path[t])
  while path[t] != source:
    t = path[t]
    targetPath.append(path[t])
  return len(targetPath)-1
~~~
Almacenes analizados desde el 21 al 30:
  - De los almacenes analizados, no se pudo sacar un resultado concreto, puesto que el recorrido que hace el backtracking es muy amplio para el grafo trabajado.
### Conclusiones
El algoritmo de Backtracking no es el idóneo, ya que no presenta el rendimiento suficiente para soportar el gráfico, y presenta una recursividad grande con la cantidad de datos brindados.
### Bibliografía
  - Peñaloza, Jorge (2010) Ruta más corta - Solución por fuerza bruta . [Recuperado de:http://jorgep.blogspot.com/2010/10/ruta-mas-corta-solucion-por-fuerza.html ]
  - Wikipedia (s.f) Vuelta atrás. [Recuperado de: https://es.wikipedia.org/wiki/Vuelta_atr%C3%A1s]
