################################################################################
# rm_longest  by Stella Gao
#
# Input
#  fasta_file:  Input FASTA file.
#
# Output
#  new fasta_file
################################################################################

def rm_longest(fasta_file):
	
	seq = ''
	header = ''
	
	for line in open(fasta_file):
		if line[0] == '>':			
			if seq:		
				if len(seq)<=10000:
					with open("NR1w.fa", "a") as f1:
						f1.write(header) 
						f1.write('\n')
						f1.write(seq)
						f1.write('\n')
				header = ''
				seq = ''
							
			header = line.rstrip()
						
		else:
			seq += line.rstrip()			
		
	if seq:
		if len(seq)<=10000:
			with open("NR1w.fa", "a") as f2:
				f2.write(header) 
				f2.write('\n')
				f2.write(seq)
				f2.write('\n')
			
	f1.close()
	f2.close()

				
				
rm_longest("NR.fa")
