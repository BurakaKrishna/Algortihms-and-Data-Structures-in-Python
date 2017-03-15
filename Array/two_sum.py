class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		if len(nums) <=1:
			return False
		hash_map = {}
		for i in range(len(nums)):
			if nums[i] in hash_map:
				return hash_map[nums[i]],i
			else:
				hash_map[target-nums[i]] = i