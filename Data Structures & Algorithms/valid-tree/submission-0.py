class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        adj = [[] for _ in range(n)]
        # Create the adjacency list
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Perform DFS for cycle detection. If cycle detected, not a tree
        visited = set() # No duplicates. Keep track of duplicates

        def dfs(node, parent):
            if node in visited:
                return False # Not a tree if have cycle (appear again)

            visited.add(node)

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue #Skip current loop if parent (original node) is its neighbor (original node's neighbor)
                if not dfs(neighbor, node):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n





        


        


        