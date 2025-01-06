class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if len(ratings) == 1:
            return 1
        def trav(lst):
            c = []
            for r in range (len(lst)):
                if r == 0:
                    if lst[r] <= lst[r+1]:
                        c.append(1)
                    else:
                        c.append(2)
                elif r == len(lst) -1 :
                    if lst[r] <= lst[r-1]:
                        c.append(1)
                    else:
                        c.append(prev+1)
                else:
                    if lst[r] == lst[r-1]:
                        c.append(1)
                    elif lst[r] > lst[r-1]:
                        c.append(prev+1)
                    else:
                        c.append(1)
                prev = c[-1]
            return c
        left_trv = trav(ratings)
        right_trv = trav(ratings[::-1])
        right_trv = right_trv[::-1]
        final_trav= []
        for k in range(len(ratings)):
            final_trav.append(max(left_trv[k], right_trv[k]))
        return sum(final_trav)