def extract_pc(output_file):
	f1 = open(output_file, "r")    
	#lines = f.readlines()
	
	f2 = open("new.fa", "w")
	
	
	for line in f1:
		if line[0] == '>':
			if line.split()[4] == "gene_biotype:protein_coding" and line.split()[5] == "transcript_biotype:protein_coding":
				f2.write(line)
				f2.write(next(f1))
		
	f1.close()
	f2.close() 
	

extract_pc('test.fa')
