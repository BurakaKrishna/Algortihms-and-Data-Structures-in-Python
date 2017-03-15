class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
        	index = abs[nums[i]]-1
        	nums[index] = -abs(nums[index])
        	return for 


# print Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])
nums = [1,2,2,4]
nums = [4,3,2,7,8,2,3,1]

for i in xrange(len(nums)):
	index = abs(nums[i]) - 1
	nums[index] = - abs(nums[index])
	print nums
print [i + 1 for i in range(len(nums)) if nums[i] > 0]
