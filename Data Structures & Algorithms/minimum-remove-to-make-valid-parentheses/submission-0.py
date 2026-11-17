class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = [] 
        count = 0
        for lett in s:
            if lett == '(':
                count += 1
                stack.append(lett)
            elif lett == ')':
                if count > 0:
                    stack.append(lett)
                    count -= 1
            else:
                stack.append(lett)
        
        if count == 0: return "".join(stack)

        for i in range(len(stack)-1,-1,-1):
            if count > 0 and stack[i] == '(':
                stack.pop(i)
                count -= 1

        return "".join(stack)
                

