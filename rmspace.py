def rmspace(fasta_file):
	seq = ''
	header = ''
	
	for line in open(fasta_file):
		if line[0] == '>' :			
			if seq:
				#print header
				with open("Human_test_rmspace.fa", "a") as f1:
					f1.write(header) 
					f1.write('\n')
					f1.write(seq)
					f1.write('\n')
				header = ''
				seq = ''
			
			header = line.rstrip()
		
		else:
			if header:
				seq += line.rstrip()
		
	if seq:
		#print header
		with open("Human_test_rmspace.fa", "a") as f1:
			f1.write(header) 
			f1.write('\n')
			f1.write(seq)
			f1.write('\n')

	
	f1.close()

				
				
rmspace('Human_test.fa')
