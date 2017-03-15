def binary(lst,target):
	if(target > lst[len(lst)-1]):
		return len(lst)
	if(target < lst[0]):
		return 0
	l,r = 0,len(lst)-1
	while l >=r:
		m=l+r/2
		if lst[m] > target:
			r = m-1
			if r>=0:
				if lst[r] < target:
					return r + 1
			else:
				return 0
		elif lst[m] > target:
			l = m+1
			if l < len(lst):
				if lst[l] > target:
					return l
			else:
				return len(lst)
		else:
			return m



