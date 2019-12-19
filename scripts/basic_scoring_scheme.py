#Input: two strings of text of equal length
#Output: similarity score s based on a +1/-1 scoring scheme

def scoring(seq1, seq2):
    s = 0
    for i in xrange(len(seq1)):
        if seq1[i] == seq2[i]: 
            s += 1
        else:
            s += -1
    return s


print(scoring('ACCTCGATCGCTAGCTAACTAGC','ACTCCGTAGGCTGCTTAGTTACC'))
print(scoring('ACCTCGATCGCTAGCTAACTAGC','ACCTCGATCGCTAGCTAACTACC'))

