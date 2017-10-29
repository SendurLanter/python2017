import sys
show=[]
def switch(x,base):
	if x!=0:
		show.append(x%base)
		x/=base
		switch(x,base)
	elif x==0:
		return 	
	return
switch(int(sys.argv[1]),int(sys.argv[2]))
show.reverse()
print show