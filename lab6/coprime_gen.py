import sys
def generator(A,x):
	count=0

	for e in range(2,x+1):
		if x%e==0 and e in A:
			count+=1
			break
	
	if count !=0:
		return generator(A,x+1)
	else:
		return x
	

def coprime_test(x,n):
	A=set()
	for e in range(2,x+1):
		if x%e==0:
			A.add(e)
	count=0
	while count<n:	
		x=generator(A,x+1)
		print x
		count+=1

coprime_test(int(sys.argv[1]),int(sys.argv[2]))



