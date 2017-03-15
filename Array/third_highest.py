def thirdMax(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	nums = list(set(nums))
	if len(nums)==2:
			return nums[0] if nums[0]>nums[1] else nums[1]
	low,med,high = nums[0],nums[0],nums[0]
	for i in range(1,len(nums)):
		if (nums[i]>med) and (nums[i]>low):
			if nums[i] > high:
				low = med
				med = high
				high = nums[i]
			if nums[i] < high:
				low = med
				med = nums[i]
		if (nums[i]>low) and (nums[i]<med):
				low = nums[i]
		if (nums[i]<low):
			if low == med or med == high:
				high = med
				med = low
				low = nums[i]
	if low == med:
		return high
	if med == high:
		return med
	# print low,med,high
	return low
# print thirdMax([1,1,2])
print thirdMax([2,2,3,1])
# print len([3,2,1])
# (nums[i]<med) and (nums[i]<high) and ((nums[i]>low) or (nums[i]<low))