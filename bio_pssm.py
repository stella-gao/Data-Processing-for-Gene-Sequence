from Bio import SeqIO

for seq_record in SeqIO.parse("nue1.txt", "fasta"):
    sq = seq_record.seq
    instances.append(sq)
    
m1 = motifs.create(instances)
# print(m)
# len(m)
score1 = m1.pssm

for seq_record in SeqIO.parse("nue2.txt", "fasta"):
    sq = seq_record.seq
    instances.append(sq)
    
m2 = motifs.create(instances)
score2 = m2.pssm
