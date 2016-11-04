################################################################################
# split_NM_NR  by Stella Gao
#
# Input
#  fasta_file:  Input FASTA file.
#
# Output
#  2 files:    NM.fa and NR.fa
################################################################################
# Separate NM and NR
def split_NM_NR(fasta_file):
	seqNM = ''
	seqNR = ''

	headerNR = ''
	headerNM = ''
	
	for line in open(fasta_file):
		if line[0] == '>' and line[1] == 'N':			
			if seqNR:
				print headerNR
				with open("NR.fa", "a") as f1:
					f1.write(headerNR) 
					f1.write('\n')
					f1.write(seqNR)
					f1.write('\n')
				headerNR = ''
				seqNR = ''
			
			if seqNM:
				print headerNM
				with open("NM.fa", "a") as f2:
					f2.write(headerNM) 
					f2.write('\n')
					f2.write(seqNM)
					f2.write('\n')
				headerNM = ''
				seqNM = ''
				
			if line[2] == 'R':
				headerNR = line.rstrip()
				
			if line[2] == 'M':
				headerNM = line.rstrip()
		
		else:
			if headerNR:
				seqNR += line.rstrip()
			if headerNM:
				seqNM += line.rstrip()
		
	if seqNR:
		#print headerNR
		with open("NR.fa", "a") as f1:
			f1.write(headerNR) 
			f1.write('\n')
			f1.write(seqNR)
			f1.write('\n')
			
	if seqNM:
		#print headerNM
		with open("NM.fa", "a") as f2:
			f2.write(headerNM) 
			f2.write('\n')
			f2.write(seqNM)
			f2.write('\n')

	
	f1.close()
	f2.close()
				
				
split_NM_NR('test.fa')
