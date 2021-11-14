
def BruteForce(G,s):
  n=len(G)
  visited=[False]*n
  m = a[s]

  for i in range (len(a)):
    if a[i] > m:
      m = a[i]
        return m
    else:
      if not visited[s]:
        visited[s] = True
        for v in G[s]:
          m.append(v)
          s = v
          BruteForce(G,s)

  return m
