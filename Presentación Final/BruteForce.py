def bruteforce(G, s):
  n = len(G)
  tvisit = [None, s]
  parent = []
  visited = [False]*n
  while(tvisit):
    v = tvisit.pop()
    if v : 
      parent.append(v)
      if len(parent) == n:
        break
      visited[v]
      for x in G[v]:
        tvisit.append(None)
        tvisit.append(x) 
  return parent

#Algoritmo Brute Force punto a punto 

def bfPointToPoint(G,s,t):
  n = len(G)
  tvisit = [None, s]
  parent = []
  visited = [False]*n
  while(tvisit):
    v = tvisit.pop()
    if v : 
      parent.append(v)
      if len(parent) == n:
        break
      visited[v]
      for x in G[v]:
        tvisit.append(None)
        tvisit.append(x) 
  return parent, parent[t]
