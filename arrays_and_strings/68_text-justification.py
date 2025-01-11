class Solution():
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def rm(rem, k):
            while rem > 0:
                for i in range(len(k)):
                    if " " in k[i]:
                        if rem:
                            k[i] += " "
                            rem -= 1
                        else:
                            break
            return k

        ls = []
        s = ""
        for w in range(len(words)):
            if not s:
                s = words[w]
            else:
                if not len(s + f" {words[w]}") > maxWidth:
                    s += f" {words[w]}"
                else:
                    rem = maxWidth - len(s)
                    k = list(s)
                    if rem:
                        k = rm(rem, k)
                    s = "".join(k)
                    ls.append(s)
                    s = words[w]
                    if w == len(words) - 1:
                        rem = maxWidth - len(words[w])
                        k = list(words[w])
                        k.append(" ")
                        rem -= 1
                        if rem:
                            k = rm(rem, k)
                        ls.append("".join(k))




                    
                    
        
sol = Solution()
sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)