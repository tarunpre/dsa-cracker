class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        # if len(nums) == 1:
        #     return 1
        # j=0
        # i=0
        # m = 0
        # while i <len(nums):
        #     if abs(max(nums[j:i+1])-min(nums[j:i+1])) <= limit:
        #         m = max(m,len(nums[j:i+1]))
        #         i += 1
        #     else:
        #         j+=1
        # return m
        mindq = deque()
        maxdq = deque()
        l = 0
        mx = 0
        for r in range(len(nums)):
            while maxdq and maxdq[-1] < nums[r]:
                maxdq.pop()
            while mindq and mindq[-1] > nums[r]:
                mindq.pop()
            maxdq.append(nums[r])
            mindq.append(nums[r])

            if maxdq[0]-mindq[0] > limit:
                if nums[l] == maxdq[0]:
                    maxdq.popleft()
                if nums[l] == mindq[0]:
                    mindq.popleft()
                l += 1
            mx = max(mx,r-l+1)
        return mx
        