class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        higher = False
        for i in range(len(temperatures)):
            higher = False
            for j in range(i, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    higher = True
                    stack.append(j-i)
                    break
            if higher == False:
                stack.append(0)
        return stack


        