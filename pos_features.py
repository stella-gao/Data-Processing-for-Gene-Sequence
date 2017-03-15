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


w1, h1 = 4, 6
pssm_nue_matrix = [[0 for x in range(w1)] for y in range(h1)]
pssm_nue_matrix = [[1,1,0,1,1,1],[0,0,1,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

w2, h2 = 4, 2
pssm_cs_matrix = [[0 for x in range(w2)] for y in range(h2)]
pssm_cs_matrix = [[0.06,0.73],[0.49,0.16],[0.31,0.06],[0.14,0.04]]
'''
A:   0.06   0.73
T:   0.49   0.16
C:   0.31   0.06
G:   0.14   0.04
'''


def short(fasta_file):
	
	seq = ''
	header = ''
	sum1 = 0
	sum2 = 0
	
	for line in open(fasta_file):
		if line[0] == '>':			
			if seq:
				ac = 0
				ga = 0
				t = 0
				gc = 0
				ag = 0
				gg = 0
				g = 0
				ta = 0
				cc = 0
				at = 0
				tt = 0
				tc = 0
				sub1 = seq[132:162]
				sub6 = seq[0:130]
				sub7 = seq[0:130]
				sub8 = seq[0:130]
				sub9 = seq[0:130]
				sub10 = seq[0:130]
				sub11 = seq[0:130]
				sub12 = seq[0:130]
				
				pssm_nue= []
				for i in range(20):
					sum = 0
					for j in range(6):
						sum += (seq[i+j]=='A') * pssm_nue_matrix[0][j] + (seq[i+j]=='T') * pssm_nue_matrix[1][j] + (seq[i+j]=='C') * pssm_nue_matrix[2][j] + (seq[i+j]=='G') * pssm_nue_matrix[3][j]
					pssm_nue.append(sum)
					
				nue = []
				for i in range(20):
					sum = 0
					if seq[i:i+6] in d.keys():
						sum = d[seq[i:i+6]]
					nue.append(sum)
				
				pssm_cs = []
				sum1 += (seq[0]=='A') * pssm_cs_matrix[0][0] + (seq[0]=='T') * pssm_cs_matrix[1][0] + (seq[0]=='C') * pssm_cs_matrix[2][0] + (seq[0]=='G') * pssm_cs_matrix[3][0]
				sum2 += (seq[1]=='A') * pssm_cs_matrix[0][1] + (seq[1]=='T') * pssm_cs_matrix[1][1] + (seq[1]=='C') * pssm_cs_matrix[2][1] + (seq[1]=='G') * pssm_cs_matrix[3][1]
				pssm_cs.append(sum1)
				pssm_cs.append(sum2)
				
				# feature1
				for index, obj in enumerate(sub1):
					if index != 29 and sub1[index]=='A' and sub1[index+1]=='C':
						ac += 1
				
				# feature2
				for index, obj in enumerate(seq):
					if index != 161 and seq[index]=='G' and seq[index+1]=='A':
						ga += 1
				
				# feature3
				for index, obj in enumerate(seq):
					if seq[index]=='A':
						t += 1

				# feature4
				for index, obj in enumerate(seq):
					if index != 161 and seq[index]=='G' and seq[index+1]=='C':
						gc += 1
				
				# feature5
				for index, obj in enumerate(seq):
					if index != 161 and seq[index]=='A' and seq[index+1]=='G':
						ag += 1
				
				# feature6
				for index, obj in enumerate(sub6):
					if index != 129 and sub6[index]=='G' and sub6[index+1]=='G':
						gg += 1
				
				# feature7
				for index, obj in enumerate(sub7):
					if sub7[index]=='G':
						g += 1
				
				# feature8
				for index, obj in enumerate(sub8):
					if index != 129 and sub8[index]=='T' and sub8[index+1]=='A':
						ta += 1
				
				# feature9
				for index, obj in enumerate(sub9):
					if index != 129 and sub9[index]=='C' and sub9[index+1]=='C':
						cc += 1
				
				# feature10
				for index, obj in enumerate(sub10):
					if index != 129 and sub10[index]=='A' and sub10[index+1]=='T':
						at += 1
				
					
				# feature11
				for index, obj in enumerate(sub11):
					if index != 129 and sub11[index]=='T' and sub11[index+1]=='T':
						tt += 1
				
				# feature12
				for index, obj in enumerate(sub12):
					if index != 129 and sub12[index]=='T' and sub12[index+1]=='C':
						tc += 1
				
				with open("pos_features.txt", "a") as f1:
					f1.write(str(ac))
					f1.write(',')
					f1.write(str(ga))
					f1.write(',')
					f1.write(str(t))
					f1.write(',')
					f1.write(str(gc))
					f1.write(',')
					f1.write(str(ag)) 
					f1.write(',')
					f1.write(str(gg)) 
					f1.write(',')
					f1.write(str(g)) 
					f1.write(',')
					f1.write(str(ta)) 
					f1.write(',')
					f1.write(str(cc)) 
					f1.write(',')
					f1.write(str(at)) 
					f1.write(',')
					f1.write(str(tt)) 
					f1.write(',')
					f1.write(str(tc)) 
					f1.write(',')
					f1.write(str(max(nue)))
					f1.write(',')
					f1.write(str(max(pssm_nue)))
					f1.write(',')
					f1.write(str(max(pssm_cs)))
					f1.write(',1\n')
					f1.close()
					
				sum1 = 0 
				sum2 = 0
				header = ''
				seq = ''
							
			header = line.rstrip()
						
		else:
			seq = line.rstrip()			
		
	if seq:	
		ac = 0
		ga = 0
		t = 0
		gc = 0
		ag = 0
		gg = 0
		g = 0
		ta = 0
		cc = 0
		at = 0
		tt = 0
		tc = 0
		sub1 = seq[132:162]
		sub6 = seq[0:130]
		sub7 = seq[0:130]
		sub8 = seq[0:130]
		sub9 = seq[0:130]
		sub10 = seq[0:130]
		sub11 = seq[0:130]
		sub12 = seq[0:130]
		
		pssm_nue= []
		for i in range(20):
			sum = 0
			for j in range(6):
				sum += (seq[i+j]=='A') * pssm_nue_matrix[0][j] + (seq[i+j]=='T') * pssm_nue_matrix[1][j] + (seq[i+j]=='C') * pssm_nue_matrix[2][j] + (seq[i+j]=='G') * pssm_nue_matrix[3][j]
			pssm_nue.append(sum)
			
		nue = []
		for i in range(20):
			sum = 0
			if seq[i:i+6] in d.keys():
				sum = d[seq[i:i+6]]
			nue.append(sum)
		
		pssm_cs = []
		sum1 += (seq[0]=='A') * pssm_cs_matrix[0][0] + (seq[0]=='T') * pssm_cs_matrix[1][0] + (seq[0]=='C') * pssm_cs_matrix[2][0] + (seq[0]=='G') * pssm_cs_matrix[3][0]
		sum2 += (seq[1]=='A') * pssm_cs_matrix[0][1] + (seq[1]=='T') * pssm_cs_matrix[1][1] + (seq[1]=='C') * pssm_cs_matrix[2][1] + (seq[1]=='G') * pssm_cs_matrix[3][1]
		pssm_cs.append(sum1)
		pssm_cs.append(sum2)
		
		# feature1
		for index, obj in enumerate(sub1):
			if index != 29 and sub1[index]=='A' and sub1[index+1]=='C':
				ac += 1
		
		# feature2
		for index, obj in enumerate(seq):
			if index != 161 and seq[index]=='G' and seq[index+1]=='A':
				ga += 1
		
		# feature3
		for index, obj in enumerate(seq):
			if seq[index]=='A':
				t += 1

		# feature4
		for index, obj in enumerate(seq):
			if index != 161 and seq[index]=='G' and seq[index+1]=='C':
				gc += 1
		
		# feature5
		for index, obj in enumerate(seq):
			if index != 161 and seq[index]=='A' and seq[index+1]=='G':
				ag += 1
		
		# feature6
		for index, obj in enumerate(sub6):
			if index != 129 and sub6[index]=='G' and sub6[index+1]=='G':
				gg += 1
		
		# feature7
		for index, obj in enumerate(sub7):
			if sub7[index]=='G':
				g += 1
		
		# feature8
		for index, obj in enumerate(sub8):
			if index != 129 and sub8[index]=='T' and sub8[index+1]=='A':
				ta += 1
		
		# feature9
		for index, obj in enumerate(sub9):
			if index != 129 and sub9[index]=='C' and sub9[index+1]=='C':
				cc += 1
		
		# feature10
		for index, obj in enumerate(sub10):
			if index != 129 and sub10[index]=='A' and sub10[index+1]=='T':
				at += 1
		
			
		# feature11
		for index, obj in enumerate(sub11):
			if index != 129 and sub11[index]=='T' and sub11[index+1]=='T':
				tt += 1
		
		# feature12
		for index, obj in enumerate(sub12):
			if index != 129 and sub12[index]=='T' and sub12[index+1]=='C':
				tc += 1
		
		with open("pos_features.txt", "a") as f1:
			f1.write(str(ac))
			f1.write(',')
			f1.write(str(ga))
			f1.write(',')
			f1.write(str(t))
			f1.write(',')
			f1.write(str(gc))
			f1.write(',')
			f1.write(str(ag)) 
			f1.write(',')
			f1.write(str(gg)) 
			f1.write(',')
			f1.write(str(g)) 
			f1.write(',')
			f1.write(str(ta)) 
			f1.write(',')
			f1.write(str(cc)) 
			f1.write(',')
			f1.write(str(at)) 
			f1.write(',')
			f1.write(str(tt)) 
			f1.write(',')
			f1.write(str(tc)) 
			f1.write(',')
			f1.write(str(max(nue)))
			f1.write(',')
			f1.write(str(max(pssm_nue)))
			f1.write(',')
			f1.write(str(max(pssm_cs)))
			f1.write(',1\n')
			f1.close()
			
	
	
				
				
short("pos-train.txt")
