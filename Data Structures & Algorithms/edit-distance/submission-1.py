class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        memo = {}

        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            
            if (i,j) in memo:
                return memo[(i, j)]
            
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                # delete or insert to word1
                res = min(dfs(i + 1, j), dfs(i, j + 1))
                # replace the character
                res = min(res, dfs(i + 1, j + 1))
                memo[(i, j)] = res + 1
            return memo[(i, j)]
        
        return dfs(0, 0)

        