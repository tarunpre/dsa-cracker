class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        #total = 0
        #size = len(derived)
        #for i in range(size):
        #    for j in range(size):
        #        if j == i:
        #            continue
        #        total = total ^ derived[j]
        #    if derived [i] == total:
        #        total = 0
        #        continue
        #    elif derived[i] != total:
        #        return False
        #return True 

        total_xor = 0 
        for num in derived: 
            total_xor ^= num
        if total_xor == 0:
            return True
        
        return False



        