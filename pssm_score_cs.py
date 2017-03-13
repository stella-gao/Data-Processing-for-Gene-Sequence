w, h = 4, 6
pssm_matrix = [[0 for x in range(w)] for y in range(h)]
pssm_matrix = [[0.06,0.73],[0.49,0.16],[0.31,0.06],[0.14,0.04]]
'''
A:   0.06   0.73
T:   0.49   0.16
C:   0.31   0.06
G:   0.14   0.04
'''

def pssm_score_cs(fasta_file):
	
	seq = ''
	header = ''
	sum1 = 0
	sum2 = 0
	
	for line in open(fasta_file):
		if line[0] == '>':			
			if seq:
				result = []
				sum1 += (seq[0]=='A') * pssm_matrix[0][0] + (seq[0]=='T') * pssm_matrix[1][0] + (seq[0]=='C') * pssm_matrix[2][0] + (seq[0]=='G') * pssm_matrix[3][0]
				sum2 += (seq[1]=='A') * pssm_matrix[0][1] + (seq[1]=='T') * pssm_matrix[1][1] + (seq[1]=='C') * pssm_matrix[2][1] + (seq[1]=='G') * pssm_matrix[3][1]
				result.append(sum1)
				result.append(sum2)
				with open("pssm-score-cs.txt", "a") as f1:
					f1.write(str(max(result)))
					f1.write('\n')
				sum1 = 0 
				sum2 = 0
				header = ''
				seq = ''
							
			header = line.rstrip()
						
		else:
			seq = line.rstrip()			
		
	if seq:	
		result = []
		sum1 += (seq[0]=='A') * pssm_matrix[0][0] + (seq[0]=='T') * pssm_matrix[1][0] + (seq[0]=='C') * pssm_matrix[2][0] + (seq[0]=='G') * pssm_matrix[3][0]
		sum2 += (seq[1]=='A') * pssm_matrix[0][1] + (seq[1]=='T') * pssm_matrix[1][1] + (seq[1]=='C') * pssm_matrix[2][1] + (seq[1]=='G') * pssm_matrix[3][1]
		result.append(sum1)
		result.append(sum2)
		with open("pssm-score-cs.txt", "a") as f1:
			f1.write(str(max(result)))
			f1.write('\n')

	
	
	f1.close()


				
				
pssm_score_cs("cs.txt")
