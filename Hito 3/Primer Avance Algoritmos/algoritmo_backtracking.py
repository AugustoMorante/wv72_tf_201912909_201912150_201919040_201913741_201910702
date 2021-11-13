def Backtracking(G, s, d):
  n = len(G)
  l = [s]
  visited = [False]*n

  for i in range(n):
    if s == d:
      return l
    else:
      if not visited[s]:
        visited[s] = True
        for v in G[s]:
          l.append(v)
          s = v
          Backtracking(G, s, d)

  return l
