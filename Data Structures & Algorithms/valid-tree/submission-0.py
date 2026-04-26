class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # no cycles
        # fully connected
        # n node -> n - 1 edges

        # n = 5
        # edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

        # base case
        if len(edges) > n - 1:
            return False 
        
        adj = {i : [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        q = deque([(0, -1)]) # (current, parent)
        visited.add(0)

        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                q.append((nei, node))
                visited.add(nei)
        
        return len(visited) == n
