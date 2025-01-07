class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        dic = {}
        fin = []
        for w in words:
            dic[w] = 0
            for k in words:
                if not w == k and w in k:
                    dic[w] += 1

        for k,v in dic.items():
            if v >= 1:
                fin.append(k)
        return fin


