class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for i,v in enumerate(nums):
            if v in dic:
                return True
            else:
                dic[v] = i
        return False