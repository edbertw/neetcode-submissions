class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m:
            return 0
        if not n:
            return 0

        memo = {}

        def dfs(i, j):
            if i < 0 or j < 0 or i > m - 1 or j > n - 1:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]

            res = dfs(i+1, j) + dfs(i, j+1)
            memo[(i, j)] = res

            return res

        return dfs(0, 0)







        