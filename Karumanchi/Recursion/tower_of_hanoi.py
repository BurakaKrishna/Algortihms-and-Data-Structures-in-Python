A = [5,4,3,2,1]
B = []
C = []

def move_tower_hanoi(n,Source,Destination,Auxillary):
	if n>=1:
		move_tower_hanoi(n-1,Source,Auxillary,Destination)
		Destination.append(Source.pop())
		print Source,Auxillary,Destination
		move_tower_hanoi(n-1,Auxillary,Destination,Source)

move_tower_hanoi(5,A,B,C)
