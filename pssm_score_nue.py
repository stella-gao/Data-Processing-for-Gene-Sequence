w, h = 4, 6
pssm_matrix = [[0 for x in range(w)] for y in range(h)]
pssm_matrix = [[1,1,0,1,1,1],[0,0,1,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

def pssm_score(fasta_file):
	
	seq = ''
	header = ''
	
	for line in open(fasta_file):
		if line[0] == '>':			
			if seq:
				result = []
				for i in range(20):
					sum = 0
					for j in range(6):
						sum += (seq[i+j]=='A') * pssm_matrix[0][j] + (seq[i+j]=='T') * pssm_matrix[1][j] + (seq[i+j]=='C') * pssm_matrix[2][j] + (seq[i+j]=='G') * pssm_matrix[3][j]
					result.append(sum)
				
				with open("pssm-score.txt", "a") as f1:
					f1.write(str(max(result)))
					f1.write('\n')
				header = ''
				seq = ''
							
			header = line.rstrip()
						
		else:
			seq = line.rstrip()			
		
	if seq:	
		result = []
		for i in range(20):
			sum = 0
			for j in range(6):
				sum += (seq[i+j]=='A') * pssm_matrix[0][j] + (seq[i+j]=='T') * pssm_matrix[1][j] + (seq[i+j]=='C') * pssm_matrix[2][j] + (seq[i+j]=='G') * pssm_matrix[3][j]
			result.append(sum)
		
		with open("pssm-score.txt", "a") as f1:
			f1.write(str(max(result)))
			f1.write('\n')

	
	
	f1.close()


				
				
pssm_score("nue.txt")
