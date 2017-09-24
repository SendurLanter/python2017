inputstream = open('ex1.txt','r')
data =inputstream.read()
suffer =[]
s1 =''
for e in data :
	if(e!=' '):
		suffer.append(e)

i=0
for e in suffer:
	print(e)
	suffer[i]=(int(e))**2
	print suffer[i]
	i+=1

suffer.append(17)
suffer.append(23)
suffer.append(46)
suffer.append(78)
suffer.append(91)

suffer.reverse()

i=0
for e in range(len(suffer)):
	s1+=str(suffer[i])
	s1+=' '
	i+=1
	
print s1
outputstream = open('ex1.txt','w')
outputstream.write(s1)
outputstream.close
inputstream.close
	