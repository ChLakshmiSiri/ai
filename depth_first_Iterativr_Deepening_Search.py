def recursiveDLS(graph,v,goal,limit):
  if v == goal:
    return 'GOAL'
  else:
    cutoff = False
    print(v, end=' ')
    for neighbour in graph[v]:
      result = recursiveDLS(graph, neighbour, goal, limit-1)
      if result == 'LIMIT':
        cutoff = True
      elif result != 'FAIL':
        return result
    return 'LIMIT' if cutoff else 'FAIL'
def IDS(graph, v, goal):
  for depth in range(100):
    result = recursiveDLS(graph, v, goal, depth)
    print()
    if result != 'LIMIT':
      return result, depth
graph = {
  'A' :['B', 'C'],
  'B' :['D','E'},
  'C' :['F'],
  'D' :['G','H'],
  'E' :[],
  'F' :['I','K']
  'G' :[],
  'H' :['L'],
  'I' :[],
  'K' :['M'],
  'L' :[],
  'M' :[]
}
s = input("Enter source node:")
g = input("Enter goal node:")
res, depth = IDS(graph, s, g)
if res == 'GOAL':
  print("GOal found at depth:", depth)
else:
  print("Goal not found")
