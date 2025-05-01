from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
  pq = [(0, 0, source)]  # (total_weight, num_edges, node)
  visited = {}

  while pq:
      weight, edges, node = heappop(pq)

      if node in visited:
          prev_weight, prev_edges = visited[node]
          if weight > prev_weight or (weight == prev_weight and edges >= prev_edges):
              continue

      visited[node] = (weight, edges)

      for neighbor, w in graph.get(node, []):
          new_weight = weight + w
          new_edges = edges + 1
          heappush(pq, (new_weight, new_edges, neighbor))

  return visited

    
    
def bfs_path(graph, source):
  parents = {source: None}
  queue = deque([source])

  while queue:
      current = queue.popleft()
      for neighbor in graph.get(current, []):
          if neighbor not in parents:
              parents[neighbor] = current
              queue.append(neighbor)

  return parents

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
  path = []
  current = destination
  while current is not None:
      path.append(current)
      current = parents.get(current)
  path.reverse()
  return ''.join(path[:-1])


