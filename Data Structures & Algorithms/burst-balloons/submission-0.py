class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0
        memo = {}
        def dfs(lst):
            if not lst:
                return 0
            if lst in memo:
                return memo[lst]
            
            max_res = 0

            for i in range(len(lst)):
                tmp = ((lst[i-1] if i-1 >= 0 else 1) * lst[i] * (lst[i+1] if i+1 < len(lst) else 1)) + dfs(lst[:i] + lst[i+1:])
                max_res = max(max_res, tmp)
            memo[lst] = max_res

            return max_res
        
        return dfs(tuple(nums))
        