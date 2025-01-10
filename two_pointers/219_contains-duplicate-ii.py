class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        st = {}
        for i in range(len(nums)):
            if nums[i] in st:
                if abs(i-st[nums[i]]) <= k:
                    return True
                else:
                    st[nums[i]] = i
            else:
                st[nums[i]] = i
        return False

        