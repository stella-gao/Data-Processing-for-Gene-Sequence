################################################################################
# extract_train_id  by Stella Gao
#
# Input
#  fasta_file:  Input FASTA file.
#
# Output
#  2 files:    pcRNA.fa and lincRNA.fa
################################################################################
# 

def extract_train_id(fasta_file):
	seqNM = ''
	seqNR = ''

	headerNR = ''
	headerNM = ''
	
	for line in open(fasta_file):
		if line[0] == '>' and (line.split()[7] == "lincRNA" or line.split()[7] == "protein_coding"):			
			if seqNR:
				print headerNR
				with open("lincRNA.fa", "a") as f1:
					f1.write(headerNR)
					f1.write('\n')
					f1.write(seqNR)
					f1.write('\n')
				headerNR = ''
				seqNR = ''
			
			if seqNM:
				print headerNM
				with open("pcRNA.fa", "a") as f2:
					f2.write(headerNM) 
					f2.write('\n')
					f2.write(seqNM)
					f2.write('\n')
				headerNM = ''
				seqNM = ''
				
			if line.split()[7] == "lincRNA":
				headerNR = line.split()[0]
				
			if line.split()[7] == "protein_coding":
				headerNM = line.split()[0]
				
		
		if line[0] != '>':
			if headerNR:
				seqNR = line.rstrip()
			if headerNM:
				seqNM = line.rstrip()
		
	if seqNR:
		#print headerNR
		with open("lincRNA.fa", "a") as f1:
			f1.write(headerNR) 
			f1.write('\n')
			f1.write(seqNR)
			f1.write('\n')
			
	if seqNM:
		#print headerNM
		with open("pcRNA.fa", "a") as f2:
			f2.write(headerNM) 
			f2.write('\n')
			f2.write(seqNM)
			f2.write('\n')

	
	f1.close()
	f2.close()
				
				
extract_train_id('gencode.v23.fa')
