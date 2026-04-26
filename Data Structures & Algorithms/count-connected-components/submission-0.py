class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        def bfs(node):
            q = deque([node])
            visited.add(node)
            while q:
                curr_node = q.popleft()
                for nei in adj[curr_node]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)

        count = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                count += 1
        
        return count