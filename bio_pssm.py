from Bio import SeqIO
from Bio import motifs

scores = []

for j in range(20):
    scores.append(0)

instances=[]
for i in range(20):
    for seq_record in SeqIO.parse("nue" + str(i+1) + ".txt", "fasta"):
        sq = seq_record.seq
        instances.append(sq)

    m = motifs.create(instances)
    scores[i] = m.pssm
    #print scores[i]

print max(scores)
    
# print(m)
# len(m)
'''
instances=[]
for seq_record in SeqIO.parse("nue2.txt", "fasta"):
    sq = seq_record.seq
    instances.append(sq)
    
m2 = motifs.create(instances)
score2 = m2.pssm
'''
