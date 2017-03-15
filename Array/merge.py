class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[:]=nums1[:m]
        nums1.extend(nums2[:n])
        nums1[:] = sorted(nums1)

nums1 = [0]
nums2 = [1]
m =0 
n =1

Solution().merge(nums1,m,nums2,n)
print nums1