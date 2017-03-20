def equilibrim(a):
	tot_sum,left_sum,right_sum = 0,0,0
	for i in xrange(0,len(a)):
		tot_sum = tot_sum + a[i]
		# print a[i],tot_sum
	# print tot_sum
	for i in xrange(0,len(a)):
		left_sum = tot_sum - a[i] - right_sum
		print a[i],left_sum,right_sum
		if left_sum == right_sum:
			return i
		else:
			right_sum = right_sum + a[i]
			print right_sum
	return -1

lst = [-1, 3, -4, 5, 1, -6, 2, 1] 
equilibrim(lst)