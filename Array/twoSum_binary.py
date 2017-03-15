class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r = 0, len(numbers)-1
        while l>=r:
            m = l+r/2
            if numbers[m] > target:
                