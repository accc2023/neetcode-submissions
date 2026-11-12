class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        left = 0
        right = 1
        res = 0
        if len(s) == 1 or len(s) == 0:
            return 0
        if x > y:
            stack = []
            for ch in s:
                if stack and stack[-1] == 'a' and ch == 'b':
                    stack.pop()
                    res += x
                else:
                    stack.append(ch) 
            
            new_s = stack
            stack2 = []
            for ch in new_s:
                if stack2 and stack2[-1] == 'b' and ch == 'a':
                    stack2.pop()
                    res += y
                else:
                    stack2.append(ch)
        else:
            stack = []
            for ch in s:
                if stack and stack[-1] == 'b' and ch == 'a':
                    stack.pop()
                    res += y
                else:
                    stack.append(ch) 
            
            new_s = stack
            stack2 = []
            for ch in new_s:
                if stack2 and stack2[-1] == 'a' and ch == 'b':
                    stack2.pop()
                    res += x
                else:
                    stack2.append(ch)
        return res
