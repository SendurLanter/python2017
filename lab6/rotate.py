inputf=open('table1.csv')
inputf2=open('table2.csv')
metrix=[]
submetrix=[]
metrix2=[]
while 1:

	buf = inputf.read(1)
	if not buf :
		break
	if buf !=',' and buf != '\n':
		submetrix.append(buf)
	if buf=='\n':
		metrix.append(submetrix)
		submetrix=[]

while 1:

	buf = inputf2.read(1)
	if not buf :
		break
	if buf !=',' and buf != '\n':
		submetrix.append(buf)
	if buf=='\n':
		metrix2.append(submetrix)
		submetrix=[]

for i in range(len(metrix)):

	for j in range(i,len(metrix)):

		if i!=j:
			metrix[i][j] , metrix[j][i] = metrix[j][i] , metrix[i][j]

EQ=True
for i in range(len(metrix)):
	for j in range(len(metrix)):
		if metrix[i][j]!= metrix2[i][j]:
			EQ=False
			break

print EQ