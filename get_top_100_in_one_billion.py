import heapq

def funnel(n, numbers):
	if n == 0: return []
	heap = numbers[:n]
	print "Original heap is %s" % heap
	heapq.heapify(heap)
	print "Heapified is %s" % heap
	for k in numbers[n:]:
		if heap[0] < k:
			print "The heap is %s" % heap
			print "The k is %s" % k
			heapq.heapreplace(heap, k)
			print "The new heap is %s" % heap
	return heap

n = 4
numbers = [3,1,4,1,5,9,2,6,5,3,5,8]

# heap = numbers[:n]
# print heap
# heapq.heapify(numbers)
# print numbers

funnel(n,numbers)