from collections import deque

def shortestPath(V, edges, start, end):
    adj_list = [[] for _ in range(V)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    visited = [False] * V
    queue = deque([(start, 0)])
    visited[start] = True
    
    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, dist + 1))
    
    return -1
