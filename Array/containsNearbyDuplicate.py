class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_table = {}
        for i,v in enumerate(nums):
            if v in hash_table and i - hash_table[v] <= k:
                return True
            else:
                hash_table[nums[i]]=i
        return False

print Solution().containsNearbyDuplicate([],0)