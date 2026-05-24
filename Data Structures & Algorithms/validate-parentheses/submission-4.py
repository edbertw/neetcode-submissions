class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {")": "(", "]": "[", "}": "{"}
        stack = []
        for i in s:
            if i not in mapper:
                stack.append(i)
            else:
                if not stack or stack[-1] != mapper[i]:
                    return False
                else:
                    stack.pop()
        return not stack





        