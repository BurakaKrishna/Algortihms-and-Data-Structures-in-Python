def fizzBuzz(n):
        """
        :type n: int
        :rtype: List[str]
        """
        return_list = []
        for i in range(1,n+1):
            if (i%3 == 0) and (i%5 ==0):
                return_list.append("FizzBuzz")
            elif (i%5 == 0):
                return_list.append("Buzz")
            elif (i%3 == 0):
                return_list.append("Fizz")
            else:
                return_list.append(str(i))
        print return_list
        return return_list

# fizzBuzz(1)

lst = [1,1,2]
# import unittest
from collections import OrderedDict

print OrderedDict.fromkeys(lst)


# class TestFizzBuzz(unittest.TestCase):

#     def test_input_one(self):
#         self.assertEqual(fizzBuzz(1), ["1"])

#     def test_input_till_three_multiples(self):
#         self.assertEqual(fizzBuzz(3),["1","2","Fizz"])

# if __name__ == '__main__':
#     unittest.main()