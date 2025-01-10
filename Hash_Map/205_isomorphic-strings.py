class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dc = {}
        for i in range(len(s)):
            if not s[i] in dc:
                if t[i] in dc.values():
                    return False
                dc[s[i]] = t[i]
            else:
                if dc[s[i]] != t[i]:
                    return False
        return True
        