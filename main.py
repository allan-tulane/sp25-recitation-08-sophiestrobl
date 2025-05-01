from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node

    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    def shortest_path_helper(visited, front):
        if len(front) == 0:
            return visited

        else:
            weighted_distance, edges, node = heappop(front)
            if node in visited:
                return shortest_path_helper(visited, front)
            else:
                visited[node] = (weighted_distance, edges)
                for neighbor, weight in graph[node]:
                    heappush(front, (weighted_distance + weight, edges + 1, neighbor))
                return shortest_path_helper(visited, front)

    front = []
    heappush(front, (0, 0, source))
    visited = dict()
    return shortest_path_helper(visited, front)






def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    visited = set()
    front = deque([source])
    parent = {}
    visited.add(source)

    while front:
        node = front.popleft()
        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                parent[i] = node
                front.append(i)
    return parent





def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }



def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    path = []
    while destination in parents:
        parent = parents[destination]
        path.append(parent)
        destination = parent
    return ''.join(reversed(path))


graph = get_sample_graph()
parents = bfs_path(graph, 's')
paths = get_path(parents, 'd')
print(paths)
