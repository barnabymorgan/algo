class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) < 2):
            return False
        
        stack = []
        dct = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        for o in s:
            if (o == '(' or o == '{' or o == '['):
                stack.append(o)
            elif(len(stack) == 0):
                return False
            else:
                p = stack.pop()
                if(dct[o] != p):
                    return False
                
        if(len(stack) == 0):
            return True
        return False