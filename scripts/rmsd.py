file=open("./RMSD.txt","r")
PDB1=[]
PDB2=[]
import math
x=PDB1
for line in file:
	word=line.split()
	if word[0]=="MODEL" and word[1]=="1":
		v=True
	if word[0]=="ATOM":
		if word[2]=="CA":
			if v==True:
				x.append((word[6],word[7],word[8]))
			else:
				x.append((word[5],word[6],word[7]))
	if word[0]=="MODEL" and word[1]=="2":
		v=False
		x=PDB2
x=0
for i in range(len(PDB1)):
	for j in range(3):
		cord1=float(PDB1[i][j])
		cord2=float(PDB2[i][j])
		t=cord1-cord2
		t=t**2
		x=x+t
rmsd=math.sqrt((x/100))
print(rmsd)