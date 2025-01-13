class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) in (1,2):
            return len(s)
        dc = {}
        rmv = 0
        for i in range(len(s)):
            if s[i] not in dc:
                dc[s[i]] = [i]
            else:
                dc[s[i]].append(i)
        
        for k, v in dc.items():
            if len(v) > 2:
                if len(v) % 2 == 0:
                    rmv += len(v) - 2
                else:
                    rmv += len(v) -1
        
        return len(s)-rmv

