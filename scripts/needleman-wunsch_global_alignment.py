'''
Global alignment:
Needleman-Wunsch algorithm
Given two sequences s1 and s2, with lengths a and b, define the matrix 
F(i,j) storing the score of the best alignment between the subsequences: 

Initialisation
F(0,0) = 0


Iteration 
                    |   F(i-1,j-1) + s(Ai,Bj)   #s function for score between Ai,Bj        
                    |    F(i-1,j) -d
   F(i,j) = Max     |    F(i,j-1) -d



Conclusion

F(a,b) the best alignment score for the global starts from indexes a,b


'''
import sys
'-----------------------'	

def simplegap(k):
    return -2
'-----------------------'

def simplescore(a,b):
    if a==b:
        return 1
    else:
        return -1
'-----------------------'

def matrixscore(a,b):
    import input_data
    matrix = input_data.PAM250_dict
    key = a + b
    if key in matrix:
        return matrix[key]
    else:
        print(key)

'-----------------------'
		
def globalign(s1,s2,sm=matrixscore, gap=simplegap):
	'''
	Calculates the global dynamic programming (scoring) matrix F
        and the associate traceback matrix P
	'''
    # each dimension includes the 0 (zero) column and row
    M = len(s1) + 1
    N = len(s2) + 1
    # generates the empty (zero) matrices
    F=[[0]*N for x in range(M)]
    P=[['0']*N for x in range(M)]
#initialization
    for i in range(1,M) : 
        F[i][0] = gap(i) #1 col init with -1,-2,-3..
        P[i][0] = 'c'
	
    for j in range(1,N):
        F[0][j] = gap(j) #1row init with -1,-2,-3...
        P[0][0] = 'r'
		
#iteration
    for i in range(1,M):
        for j in range(1,N):
            sR=F[i][j-1] + gap(1)
            sC=F[i-1][j] + gap(1)
            sD=F[i-1][j-1] + sm(s1[i-1], s2[j-1])	
#F[i][j] = max(sR,sC,sD)
            F[i][j], P[i][j] = max(list(zip((sR,sC,sD),("r","c","D"))))
      
    return F, P


def return_align(f, p, s1, s2):
    '''
    The function aligns s1 and s2 using p.
    f is only needed to get the alignment score sc = f[i][j]
    '''
    #start from the bottom-right cell of f and p
    i = len(p)-1
    j = len(p[0])-1
    sc = f[i][j]
    temp = ''
    targ = ''
    while i!=0 and j!=0 :
        if p[i][j]=='D':
            temp = temp + s1[i-1]
            targ = targ + s2[j-1]
            i=i-1 
            j=j-1
        elif p[i][j] == 'c': 		
            temp = temp + s1[i-1]
            targ = targ + '-'
            i = i-1
        else:
            temp=temp + '-'
            targ = targ + s2[j-1]
            j = j-1
    print(temp[::-1])
    print(targ[::-1])
    print ('score = ', sc)


# Main Program #


if __name__== '__main__':	
	
    s1 = "GSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKL"
    s2 = "GNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKL"

    if len(sys.argv) >= 3:
        s1 = sys.argv[1]
        s2 = sys.argv[2]

    print('s1 = ', s1, '\n' + 's2 = ', s2)

    f,p = globalign(s1,s2)

    return_align(f,p,s1,s2)

'''
    #this is if you want to print f and p
    for i in range(len(f)):
        for j in range(len(f[0])):
            print("%2.2f" % f[i][j], end=' ')
        print("\n")	 
		
    for i in range(len(p)):
        for j in range(len(p[0])):
            print("%3s" % p[i][j], end=' ') 
        print("\n")

'''

