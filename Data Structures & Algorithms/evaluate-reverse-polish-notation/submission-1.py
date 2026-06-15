class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            elif token == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(a+b))
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b-a))
            elif token == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(a*b))
            else:
                stack.append(int(token))
            
        return stack[0]
            
                