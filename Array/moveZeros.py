class Solution(object):
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		for i in range(nums.count(0)):
			nums.remove(0)
			nums.append(0)
		return nums

print Solution().moveZeroes([1,3,12,0,0])