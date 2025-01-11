class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if len(s) < k:
            return False
        cnt_dic = {}
        odd = []
        for t in s:
            if t in cnt_dic:
                cnt_dic[t] += 1
            else:
                cnt_dic[t] = 1
        for i,v in cnt_dic.items():
            if v % 2 != 0:
                odd.append(i)
        print(odd)
        if len(odd) > k:
            return False
        return True