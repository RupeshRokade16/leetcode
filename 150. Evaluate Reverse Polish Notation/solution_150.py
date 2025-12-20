class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {"+","-","*","/"}

        def operation(char, a, b):
            if char == "+":
                return a + b
            if char == "-":
                return a - b
            if char == "*":
                return a * b
            if char == "/":
                return int(a/b)

        i = 0
        while i < len(tokens):
            if tokens[i] in operands:
                #Pop from stack and compute and add back to stack and increment i
                b = stack.pop() #Need to be careful with the order 
                                #since division is a possible operand
                a = stack.pop()
                value = operation(tokens[i], a, b)
                i += 1
                stack.append(value)
            else:
                stack.append(int(tokens[i]))
                i += 1
        return stack[-1]

        