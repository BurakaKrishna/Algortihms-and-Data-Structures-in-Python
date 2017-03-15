class Solution(object):
	def findMaxConsecutiveOnes(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		count,state = 0,0
		for num in nums:
			if num == 1:
				count = count+1
				if count > state:
					state = count
			else:
				count = 0
		return state

nums=[1,0,1,1,0,1]
print Solution().findMaxConsecutiveOnes(nums)