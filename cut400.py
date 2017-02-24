def cut(fasta_file):
	
	seq = ''
	header = ''
	
	for line in open(fasta_file):
		if line[0] == '>':			
			if seq:		
				n = len(seq)/400
				with open("TAIR_5_utr_400.fa", "a") as f1:
					for i in range(n):
						f1.write(header) 
						f1.write('\n')
						f1.write(seq[400*i:400*i+400])
						f1.write('\n')
				header = ''
				seq = ''
							
			header = line.rstrip()
						
		else:
			seq = line.rstrip()			
		
	if seq:
		n = len(seq)/400
		with open("TAIR_5_utr_400.fa", "a") as f1:
			for i in range(n):
				f1.write(header) 
				f1.write('\n')
				f1.write(seq[400*i:400*i+400])
				f1.write('\n')
	
	
	f1.close()


				
				
cut("TAIR_5_utr_long.fa")
