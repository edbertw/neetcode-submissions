class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        2D DP problem

        '''
        if not text1:
            return 0
        if not text2:
            return 0
        
        memo = {}

        def dfs(i, j):
            if i == -1 or j == -1:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]
            
            res = 0
            
            if text1[i] == text2[j]:
                res = 1 + dfs(i-1, j-1)
            else:
                res = max(dfs(i-1, j), dfs(i, j-1))
            
            memo[(i, j)] = res

            return res

        return dfs(len(text1) - 1, len(text2) - 1)
        

                

            
        