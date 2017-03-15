class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k] 

nums = [1]
k = 0
print Solution().rotate(nums,k)
			