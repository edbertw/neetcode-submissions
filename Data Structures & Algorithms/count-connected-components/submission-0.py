class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n
        # undirected graph
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def bfs(node):
            q = deque([node])
            while q:
                cur = q.popleft()
                for nei in adj[cur]:
                    if not visited[nei]:
                        visited[nei] = True
                        q.append(nei)
        
        res = 0
        for node in range(n):
            if not visited[node]:
                bfs(node)
                res += 1
        return res


        
        