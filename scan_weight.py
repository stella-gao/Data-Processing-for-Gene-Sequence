import xlrd

d = {}
wb = xlrd.open_workbook('weight.xlsx')
sh = wb.sheet_by_index(0)
for i in range(50):
	cell_value = sh.cell(i,1).value
	cell_value_id = sh.cell(i,0).value
	d[cell_value_id] = cell_value
	# print cell_value
	# print cell_value_id

def weight_score(fasta_file):
	
	seq = ''
	header = ''
	
	for line in open(fasta_file):
		if line[0] == '>':			
			if seq:
				result = []
				for i in range(20):
					sum = 0
					if seq[i:i+6] in d.keys():
						sum = d[seq[i:i+6]]
					result.append(sum)
				
				with open("nue-weight-score.txt", "a") as f1:
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
			if seq[i:i+6] in d.keys():
				sum = d[seq[i:i+6]]
			result.append(sum)
		
		with open("nue-weight-score.txt", "a") as f1:
			f1.write(str(max(result)))
			f1.write('\n')

	
	
	f1.close()

				
weight_score("nue.txt")
