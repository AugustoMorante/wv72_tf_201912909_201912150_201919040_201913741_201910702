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

#Algoritmo Brute Force punto a punto 

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

