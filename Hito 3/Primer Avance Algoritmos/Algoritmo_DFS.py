def dfs(G, s):
  n = len(G)
  visited = [False]*n
  parent = [None]*n
  stack = [s]

  while stack:
    u = stack.pop()
    if not visited[u]:
      visited[u] = True
      for v in G[u]:
        if not visited[v]:
          parent[v] = u
          stack.append(v)

  return parent