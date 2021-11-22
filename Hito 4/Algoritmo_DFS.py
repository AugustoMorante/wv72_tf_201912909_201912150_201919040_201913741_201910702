import graphviz as gv
import numpy as np
import pandas as pd
import heapq as hq
import math

def readAdjl(fn, haslabels=False, weighted=False, sep="|"):
  with open(fn) as f:
    labels = None
    if haslabels:
      labels = f.readline().strip().split()
    L = []
    for line in f:
      if weighted:
        L.append([tuple(map(int, p.split(sep))) for p in line.strip().split()])
        # line => "1|3 2|5 4|4" ==> [(1, 3), (2, 5), (4, 4)]
      else: 
        L.append(list(map(int, line.strip().split()))) # "1 3 5" => [1, 3, 5]
        # L.append([int(x) for x in line.strip().split()])
  return L, labels

def adjlShow(L, labels=None, directed=False, weighted=False, path=[],
             layout="sfdp"):
  g = gv.Digraph("G") if directed else gv.Graph("G")
  g.graph_attr["layout"] = layout
  g.edge_attr["color"] = "gray"
  g.node_attr["color"] = "orangered"
  g.node_attr["width"] = "0.1"
  g.node_attr["height"] = "0.1"
  g.node_attr["fontsize"] = "8"
  g.node_attr["fontcolor"] = "mediumslateblue"
  g.node_attr["fontname"] = "monospace"
  g.edge_attr["fontsize"] = "8"
  g.edge_attr["fontname"] = "monospace"
  n = len(L)
  for u in range(n):
    g.node(str(u), labels[u] if labels else str(u))
  added = set()
  for v, u in enumerate(path):
    if u != None:
      if weighted:
        for vi, w in G[u]:
          if vi == v:
            break
        g.edge(str(u), str(v), str(w), dir="forward", penwidth="2", color="orange")
      else:
        g.edge(str(u), str(v), dir="forward", penwidth="2", color="orange")
      added.add(f"{u},{v}")
      added.add(f"{v},{u}")
  if weighted:
    for u in range(n):
      for v, w in L[u]:
        if not directed and not f"{u},{v}" in added:
          added.add(f"{u},{v}")
          added.add(f"{v},{u}")
          g.edge(str(u), str(v), str(w))
        elif directed:
          g.edge(str(u), str(v), str(w))
  else:
    for u in range(n):
      for v in L[u]:
        if not directed and not f"{u},{v}" in added:
          added.add(f"{u},{v}")
          added.add(f"{v},{u}")
          g.edge(str(u), str(v))
        elif directed:
          g.edge(str(u), str(v))
  return g

def crearGrafoVersion1(n):
  t = [[] for i in range(n**2)]
  for i in range(n**2):
    if i == 0:
      t[i].append([i,i+1])
      t[i].append([i,i+n])
    elif i in range(1,n-1):
      t[i].append([i,i-1])
      t[i].append([i,i+1])
      t[i].append([i,i+n])
    elif i == n-1:
      t[i].append([i,i-1])
      t[i].append([i,i+n])
    elif i%n == 0 and i != 0 and i != n*(n-1):
      t[i].append([i,i+1])
      t[i].append([i,i+n])
      t[i].append([i,i-n])
    elif (i+1)%n == 0 and i != n-1 and i != (n**2)-1:
      t[i].append([i,i-1])
      t[i].append([i,i+n])
      t[i].append([i,i-n])
    elif i == n*(n-1):
      t[i].append([i,i+1])
      t[i].append([i,i-n])
    elif i in range(n*(n-1)+1,(n**2)-1):
      t[i].append([i,i-1])
      t[i].append([i,i+1])
      t[i].append([i,i-n])
    elif i == (n**2)-1:
      t[i].append([i,i-1])
      t[i].append([i,i-n])
    else:
      t[i].append([i,i-1])
      t[i].append([i,i+1])
      t[i].append([i,i+n])
      t[i].append([i,i-n])

  return t


t = crearGrafoVersion1(10)
t


fichero = open("1.txt", 'w')
for i in range(len(t)):
    for j in range(len(t[i])):
      fichero.write(str(t[i][j][1]) + '|1' + " ")
    fichero.write('\n')
fichero.close()


G, _ = readAdjl("1.txt", weighted=True) ##Cuando quiera leer de otro archivo .txt cambia el nombre de "1.txt" x el de tu archivo
for i, edges in enumerate(G):
  print(f"{i:2}: {edges}")
adjlShow(G, weighted=True)


def removeCost(G):
  re = []
  plo = []
  for i, edges in enumerate(G):
    for j in edges:
      PL.append(j[0])
    re.append(plo)
    plo = []
  return re


G = removeCost(G)

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


for i in range(5):
  path = dfs(G,i)
  print(path)