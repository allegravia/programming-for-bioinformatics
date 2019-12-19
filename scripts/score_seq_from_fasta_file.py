#Input: two strings of text of equal length from fasta file
#Output: similarity score s based on a +1/scoring scheme

def scoring(seq1, seq2):
    s = 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            s += 1
        else:
            s += -1
    return s


def read_input(fasta_file):
    seqs = []
    fasta = open(fasta_file)
    for line in fasta:
        if not line.startswith('>'):
            seqs.append(line.strip())
    return seqs
            
seqs = read_input('data/hba_hbb_human.fasta')
print seqs

if len(seqs) == 2:
    print "the scoring of the alignment is: ", scoring(seqs[0], seqs[1])
else:
    print "too many sequences in the array"



        

