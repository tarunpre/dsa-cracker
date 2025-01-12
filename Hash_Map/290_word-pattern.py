class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dc  = {}
        k = s.split(" ")
        if len(pattern) != len(k):
            return False
        for p in range(len(pattern)):
            if pattern[p] not in dc:
                if k[p] not in dc.values():
                    dc[pattern[p]] = k[p]
                else:
                    return False
            else:
                if not dc[pattern[p]] == k[p]:
                    return False
        return True
