def rmlines(output_file):
	f = open(output_file, "r")    
	lines = f.readlines()
	f.close()
	
	rm_lines_after = 4772603
	
	f = open(output_file, "w")
	
	cnt = 0
	for line in lines:
		cnt += 1
		if cnt <= rm_lines_after:
			f.write(line)
		
	f.close() 
	

rmlines('Homo_sapiens.GRCh38.cdna.all.fa')
