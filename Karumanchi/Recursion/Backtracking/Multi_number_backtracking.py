A= [None]*5
k = 2
def Multi_bit_generator(n):
	if n<1:
		print A
	else:
		for i in xrange(k):
			A[n-1] = i
			Multi_bit_generator(n-1)

Multi_bit_generator(5)
