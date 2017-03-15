lst = [1,2,3,6]

def dummy(lst,number):
	try:
		print lst.index(number)
	except ValueError:
		print find_index(lst,number) 

def find_index(lst,number):
	if max(lst) > number:
		for i in range(0,len(lst)):
			if(lst[i] > number):
				return i
			else:
				i = i+1
	else:
		return len(lst)

# dummy(lst,7)
# dummy(lst,3)
# dummy(lst,5)

class Solution(object):
	def searchInsert(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		try:
			print lst.index(target)
		except ValueError:
			print Solution.find_index(lst,target)

	@classmethod
	def find_index(cls,lst,target):
		if max(lst) > target:
			for i in range(0,len(lst)):
				if(lst[i] > target):
					return i
				else:
					i = i+1
		else:
			return len(lst)

Solution().searchInsert(lst,4)






import unittest

# class TestFizzBuzz(unittest.TestCase):

#     def test_input_one(self):
#         self.assertEqual(fizzBuzz(1), ["1"])

#     def test_input_till_three_multiples(self):
#         self.assertEqual(fizzBuzz(3),["1","2","Fizz"])

# if __name__ == '__main__':
#     unittest.main()