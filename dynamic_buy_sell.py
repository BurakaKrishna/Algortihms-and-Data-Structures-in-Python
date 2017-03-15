class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if len(prices):
			high = 0
			small = prices[0]
			for price in prices:
				if price < small:
					small = price
				if price >= small:
					if price-small > high:
						high = price-small
		return high

prices = [7,1,5,3,6,4]
print Solution().maxProfit(prices)        
