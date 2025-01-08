class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(s1, s2):
            if len(s1) <= len(s2):
                n = len(s1)
                if s1 == s2[:n] and s1 == s2[-n:]:
                    return True
            return False
        o = 0
        ln = len(words)
        for i in range(ln):
            for x in range(len(words[i+1:])):
                if isPrefixAndSuffix(words[i], words[i+1:][x]):
                    o += 1
        return o