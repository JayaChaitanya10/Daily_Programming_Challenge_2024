def hasCycle(V, edges):
    def dfs(v, parent):
        visited[v] = True
        for neighbor in adj_list[v]:
            if not visited[neighbor]:
                if dfs(neighbor, v):
                    return True
            elif neighbor != parent:
                return True
        return False
    
    adj_list = [[] for _ in range(V)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False
