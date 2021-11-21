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
