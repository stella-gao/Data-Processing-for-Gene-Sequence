def rmspace(fasta_file):
	seq = ''
	header = ''
	cnt = 0
	
	for line in open(fasta_file):
		cnt += 1
		if line[0] == '>' :			
			if seq:
				if header[3] == '3':
					with open("TAIR_cds_400_3.fa", "a") as f1:
						f1.write(header) 
						f1.write('\n')
						f1.write(seq)
						f1.write('\n')
						f1.close()
				else:
					with open("TAIR_cds_400_1245.fa", "a") as f1:
						f1.write(header) 
						f1.write('\n')
						f1.write(seq)
						f1.write('\n')
						f1.close()
				header = ''
				seq = ''
			
			header = line.rstrip()
		
		else:
			if header:
				seq += line.rstrip()
		
	if seq:
		if header[3] == '3':
			with open("TAIR_cds_400_3.fa", "a") as f1:
				f1.write(header) 
				f1.write('\n')
				f1.write(seq)
				f1.write('\n')
				f1.close()
		else:
			with open("TAIR_cds_400_1245.fa", "a") as f1:
				f1.write(header) 
				f1.write('\n')
				f1.write(seq)
				f1.write('\n')
				f1.close()
				
				
rmspace('TAIR_cds_400.fa')
