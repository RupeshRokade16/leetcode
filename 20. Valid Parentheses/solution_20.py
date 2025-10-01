class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        closeToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for char in s:
            #if char is an open bracket
            if char not in closeToOpen:
                stack.append(char)

            #if char is a closed bracket
            else:
                if stack and (stack[-1] == closeToOpen[char]):
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False
