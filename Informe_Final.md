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
