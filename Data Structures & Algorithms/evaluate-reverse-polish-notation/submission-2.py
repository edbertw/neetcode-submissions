class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = 0
        stack = []
        operators = ["+", "-", "*", "/"]
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                first = stack.pop()
                second = stack.pop()
                if i == "+":
                    result = first + second
                elif i == "-":
                    result = second - first
                elif i == "*":
                    result = second * first
                else:
                    result = int(float(second) / first)
                stack.append(result)
        return int(stack[0])



        