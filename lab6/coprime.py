import sys
def coprime_test(x,y):
	A=set()
	B=set()
	for e in range(2,x+1):
		if x%e==0:
			A.add(int(e))
	for e in range(2,y+1):
		if y%e==0:
			B.add(int(e))
	if not A&B:
		return True	
	else:
		return False
print coprime_test(int(sys.argv[1]),int(sys.argv[2]))