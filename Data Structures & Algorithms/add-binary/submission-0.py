class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        a,b = a[::-1], b[::-1]
        carry = 0

        for i in range(0,max(len(a),len(b))):
            valA = int(a[i]) if i < len(a) else 0
            valB = int(b[i]) if i < len(b) else 0

            total = valA + valB + carry
            char = str(total % 2)
            carry = total // 2
            res = char + res

        if carry == 1: res = "1" + res
        return res