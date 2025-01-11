class Solution():
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ls = []
        s = ""
        for w in range(len(words)):
            if not s:
                s = words[w]
            else:
                if len(s) + 1 + len(words[w]) <= maxWidth:
                    s += " "
                    s += words[w]
                else:
                    ls.append(s)
                    s = words[w]
                if w == len(words) -1 :
                    ls.append(s)
        if s and not ls:
            ls.append(s)
        for l in range(len(ls)):
            rem = maxWidth - len(ls[l])
            if rem: 
                if " " in ls[l] and l != len(ls)-1:
                    k = list(ls[l])
                    ind = [j for j in range(len(k)) if " " in k[j]]
                    while rem > 0:
                        for m in ind:
                            if rem:
                                k[m] += " "
                                rem -= 1
                    ls[l] = "".join(k)
                else:
                    k = list(ls[l])
                    while rem > 0:
                        k.append(" ")
                        rem -= 1
                    ls[l]="".join(k)
        return ls
sol = Solution()
#sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
sol.fullJustify(["What","must","be","acknowledgment","shall","be"], 16)