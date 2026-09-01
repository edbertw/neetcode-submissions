class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        memo = {}

        def dfs(i, j, k):
            if k == -1:
                return (i == -1) and (j == -1)
            
            if (i, j) in memo:
                return memo[(i, j)]

            res = False
            
            if i > -1 and s1[i] == s3[k]:
                res = dfs(i - 1, j, k - 1)
            if not res and j > -1 and s2[j] == s3[k]:
                res = dfs(i, j - 1, k - 1)
            
            memo[(i, j)] = res
            return res

        return dfs(len(s1) - 1, len(s2) - 1, len(s3) - 1)

        