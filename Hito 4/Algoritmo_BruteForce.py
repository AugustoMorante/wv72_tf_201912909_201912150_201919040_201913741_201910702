
def BruteForce(G,s):
  n=len(G)
  visited=[False]*n
  f = [None]*n
  m = a[s]

    if a[i] > m:
      m = a[i]

    else:
      if not visited[s]:
        visited[s] = True
        for v in G[s]:
          m.append(v)
          s = v
          BruteForce(G,s)

  return m
