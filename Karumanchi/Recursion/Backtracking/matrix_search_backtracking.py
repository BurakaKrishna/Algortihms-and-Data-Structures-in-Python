import numpy as np
import pdb
backtrack = []

def getval(matrix,i,j,row_size,col_size):
	if (i>=row_size or i<0 or j<0 or j>=col_size):
		return 0
	else:
		return matrix[i,j]

def findmaxsumpath(matrix,maxsize,size,i,j,row_size,col_size,track_matrix):
	# top find the max path
	# pdb.set_trace()
	# print ('The passed on size is %s' %size)
	if (i>=row_size) or (j>=col_size):
		# printing ('something something dark side')
		return
	track_matrix[i,j] = True
	size = size+1
	# print ('Size is %s'%size)
	# print ('Max_Size is %s'%maxsize)
	if size > maxsize:
		maxsize = size
	# print ('Resulting maxsize is %s' %maxsize)
	directions = [[-1,-1],[-1,0],[1,1],[1,0],[0,1],[-1,1],[0,-1],[1,-1]]
	for m in range(8):
		# print (i,j,m)
		new_i = i + directions[m][0]
		new_j = j + directions[m][1]
		# print(maxsize,size,m,i,j)
		# print ('The get val is %s'% getval(matrix,new_i,new_j,row_size,col_size))
		# print ('The tracking is %s'%new_i,new_j)
		val = getval(matrix,new_i,new_j,row_size,col_size)
		if val >0 and track_matrix[new_i,new_j] == False:
			# print ('Something is happening')
			findmaxsumpath(matrix,maxsize,size,new_i,new_j,row_size,col_size,track_matrix)
	track_matrix[i,j] = False
	backtrack.append(maxsize)

def maxcount(matrix,row_size,col_size):
	# create a bool matrix to maintain state while backtracking
	size = 0
	maxsize = 0
	track_matrix = np.matrix(np.zeros((row_size,col_size),dtype=bool))
	for i in range(row_size):
		for j in range(col_size):
			if matrix[i,j] == 1:
				findmaxsumpath(matrix,maxsize,size,i,j,row_size,col_size,track_matrix)
	print (max(backtrack))

mat = np.matrix([[1,1,0,0,0],[0,1,1,0,0],[0,0,1,0,1],[1,0,0,0,1],[0,1,0,1,1]])
maxcount(mat,5,5)
# print (max(backtrack))