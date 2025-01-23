class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
            return False
        if x < 10:
            return True
        c = 0
        temp = x
        while temp!=0:
            r = temp%10
            temp = temp//10
            if not c:
                c = r
            else:
                c = c*10+r
        if c == x:
            return True
        return False
            


        