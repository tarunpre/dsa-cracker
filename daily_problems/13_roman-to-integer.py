class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dictionary for all rkman and te=heir specific values
        dic = {
            "I": 1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M": 1000
        }
        n = len(s)
        if n == 1:
            return dic[s]
        val = []
        for i in range (n):
            if i > 0:
                #check
                if dic[s[i]] > dic[s[i-1]]:
                    tv = val.pop()
                    val.append(dic[s[i]]-tv)
                else:
                    val.append(dic[s[i]])
            else:
                val.append(dic[s[i]])
        return sum(val)
