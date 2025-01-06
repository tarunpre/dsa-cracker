class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # # set for prefix
        # fin = ""
        # temp = strs[0]
        # for t in range(len(temp)):
        #     c = 0
        #     for k in range(len(strs)):
        #         if t <= len(strs[k]) -1:
        #             if temp[t] == strs[k][t]:
        #                 c += 1
        #     if c == len(strs):
        #         fin += temp[t]
        #     else:
        #         break
        # return fin
        fin = []
        for x in zip(*strs):
            if len(set(x)) == 1:
                fin.append(x[0])
            else:
                break
        return "".join(fin)