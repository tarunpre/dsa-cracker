class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        #initiate empty array
        lens = len(s)
        darr = [0] * lens
        for k in shifts:
            if k[2] == 1:
                #forward
                darr[k[0]] += 1
                if k[1] + 1 < lens:
                    darr[k[1]+1] -= 1
            else:
                #backward
                darr[k[0]] -= 1
                if k[1] + 1 < lens:
                    darr[k[1]+1] += 1
        j = ""
        prev = 0
        for m in range(lens):
            prev +=  darr[m]
            cr_val = ord(s[m]) - ord('a') + prev
            cr_val %= 26
            j += chr(ord('a') + cr_val)
        return j
sol = Solution()

res = sol.shiftingLetters("abc", [[0,0,1]])
print(res)