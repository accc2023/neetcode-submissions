class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s): return False
        if len(s) == 0: return True
        ps, pt = 0,0

        while pt < len(t):
            if ps < len(s) and t[pt] == s[ps]:
                ps += 1
            pt += 1

        return ps == len(s)