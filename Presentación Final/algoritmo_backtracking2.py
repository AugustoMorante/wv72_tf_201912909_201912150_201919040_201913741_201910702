def Backtracking(G, s):
  n = len(G)
  visited = [False]*n
  f = [None]*n

  def Backtracking1(e):
    visited[e] = True
    for v in G[e]:
      if not visited[v]:
        f[v] = e
        Backtracking1(v)

  Backtracking1(s)

  return f

"""Algoritmo Punto a Punto"""

def bfsPointToPoint(G, s, t):
  n = len(G)
  visited = [False]*n
  parent = [None]*n
  
  def Backtracking1(e, t):
    visited[e] = True
    if e != t and visited[t] == False:
      for v in G[e]:
        if not visited[v]:
          parent[v] = e
          Backtracking1(v, t)

  Backtracking1(s, t)

  return parent
