# https://leetcode.com/problems/count-vowel-strings-in-ranges


class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        wv = []
        qr = []
        vowels = ['a','e','i','o','u']
        s = 0
        for w in range(len(words)):
            if words[w][0] in vowels and words[w][-1] in vowels:
                s += 1
                wv.append(s)
            else:
                wv.append(s)
        for q in range(len(queries)):
            ui = queries[q][1]
            li = queries[q][0]
            uv = wv[ui]
            lv = wv[li-1]
            if li == 0:
                lv = 0
            qr.append(uv - lv)
        return qr

# T = O(n + m)
# S = O(n + m)