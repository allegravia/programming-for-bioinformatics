#Input: two strings of text of equal length from fasta file
#Output: similarity score s based on BLOSUM50

blosum50 = {'AA': 5, 'AR':-2, 'AN':-1, 'AD':-2, 'AC':-1, 'AQ':-1,'AE':-1,
            'AG': 0, 'AH':-2, 'AI':-1, 'AL':-2, 'AK':-1, 'AM':-1,'AF':-3, 
            'AP':-1, 'AS': 1, 'AT': 0, 'AW':-3, 'AY':-2, 'AV': 0}



def scoring(seq1, seq2):
    s = 0
    for i in range(len(seq1)):
        blosum_key = seq1[i]+seq2[i]
        if blosum50.has_key(blosum_key):
            s = s + blosum50[blosum_key]
            print s
    return s


def read_input(fasta_file):
    seqs = []
    fasta = open(fasta_file)
    for line in fasta:
        if not line.startswith('>'):
            seqs.append(line.strip())
    return seqs
            
#seqs = read_input('data/hba_hbb_human.fasta')
#print seqs

seqs = ['AAAAAAAAAAAAAA','ASAVHLNRLITRLYP']

if len(seqs) == 2:
    print "the scoring of the alignment is: ", scoring(seqs[0], seqs[1])
else:
    print "too many sequences in the array"



        


