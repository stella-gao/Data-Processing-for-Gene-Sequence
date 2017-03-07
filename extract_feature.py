def features(fasta_file):
	
	seq = ''
	header = ''
	
	
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
				
				# feature1
				for index, obj in enumerate(sub1):
					if index != 29 and sub1[index]=='A' and sub1[index+1]=='C':
						ac += 1
				
				with open("feature1.txt", "a") as f1:
					f1.write(str(ac))
					f1.write('\n')
					f1.close()
					
				# feature2
				for index, obj in enumerate(seq):
					if index != 161 and seq[index]=='G' and seq[index+1]=='A':
						ga += 1
				
				with open("feature2.txt", "a") as f1:
					f1.write(str(ga))
					f1.write('\n')
					f1.close()
					
				# feature3
				for index, obj in enumerate(seq):
					if seq[index]=='A':
						t += 1
				
				with open("feature3.txt", "a") as f1:
					f1.write(str(t))
					f1.write('\n')
					f1.close()
					
				# feature4
				for index, obj in enumerate(seq):
					if index != 161 and seq[index]=='G' and seq[index+1]=='C':
						gc += 1
				
				with open("feature4.txt", "a") as f1:
					f1.write(str(gc))
					f1.write('\n')
					f1.close()
					
				# feature5
				for index, obj in enumerate(seq):
					if index != 161 and seq[index]=='A' and seq[index+1]=='G':
						ag += 1
				
				with open("feature5.txt", "a") as f1:
					f1.write(str(ag)) 
					f1.write('\n')
					f1.close()
				
				# feature6
				for index, obj in enumerate(sub6):
					if index != 129 and sub6[index]=='G' and sub6[index+1]=='G':
						gg += 1
				
				with open("feature6.txt", "a") as f1:
					f1.write(str(gg)) 
					f1.write('\n')
					f1.close()
					
				# feature7
				for index, obj in enumerate(sub7):
					if sub7[index]=='G':
						g += 1
				
				with open("feature7.txt", "a") as f1:
					f1.write(str(g)) 
					f1.write('\n')
					f1.close()
					
				# feature8
				for index, obj in enumerate(sub8):
					if index != 129 and sub8[index]=='T' and sub8[index+1]=='A':
						ta += 1
				
				with open("feature8.txt", "a") as f1:
					f1.write(str(ta)) 
					f1.write('\n')
					f1.close()
					
				# feature9
				for index, obj in enumerate(sub9):
					if index != 129 and sub9[index]=='C' and sub9[index+1]=='C':
						cc += 1
				
				with open("feature9.txt", "a") as f1:
					f1.write(str(cc)) 
					f1.write('\n')
					f1.close()
					
				# feature10
				for index, obj in enumerate(sub10):
					if index != 129 and sub10[index]=='A' and sub10[index+1]=='T':
						at += 1
				
				with open("feature10.txt", "a") as f1:
					f1.write(str(at)) 
					f1.write('\n')
					f1.close()
					
				# feature11
				for index, obj in enumerate(sub11):
					if index != 129 and sub11[index]=='T' and sub11[index+1]=='T':
						tt += 1
				
				with open("feature11.txt", "a") as f1:
					f1.write(str(tt)) 
					f1.write('\n')
					f1.close()
					
				# feature12
				for index, obj in enumerate(sub12):
					if index != 129 and sub12[index]=='T' and sub12[index+1]=='C':
						tc += 1
				
				with open("feature12.txt", "a") as f1:
					f1.write(str(tc)) 
					f1.write('\n')
					f1.close()
					
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
		
		# feature1
		for index, obj in enumerate(sub1):
			if index != 29 and sub1[index]=='A' and sub1[index+1]=='C':
				ac += 1
		
		with open("feature1.txt", "a") as f1:
			f1.write(str(ac)) 
			f1.write('\n')
			f1.close()
			
		# feature2
		for index, obj in enumerate(seq):
			if index != 161 and seq[index]=='G' and seq[index+1]=='A':
				ga += 1
		
		with open("feature2.txt", "a") as f1:
			f1.write(str(ga)) 
			f1.write('\n')
			f1.close()
			
		# feature3
		for index, obj in enumerate(seq):
			if seq[index]=='A':
				t += 1
		
		with open("feature3.txt", "a") as f1:
			f1.write(str(t)) 
			f1.write('\n')
			f1.close()
			
		# feature4
		for index, obj in enumerate(seq):
			if index != 161 and seq[index]=='G' and seq[index+1]=='C':
				gc += 1
		
		with open("feature4.txt", "a") as f1:
			f1.write(str(gc)) 
			f1.write('\n')
			f1.close()
			
		# feature5
		for index, obj in enumerate(seq):
			if index != 161 and seq[index]=='A' and seq[index+1]=='G':
				ag += 1
		
		with open("feature5.txt", "a") as f1:
			f1.write(str(ag)) 
			f1.write('\n')
			f1.close()
		
		# feature6
		for index, obj in enumerate(sub6):
			if index != 129 and sub6[index]=='G' and sub6[index+1]=='G':
				gg += 1
		
		with open("feature6.txt", "a") as f1:
			f1.write(str(gg)) 
			f1.write('\n')
			f1.close()
			
		# feature7
		for index, obj in enumerate(sub7):
			if sub7[index]=='G':
				g += 1
		
		with open("feature7.txt", "a") as f1:
			f1.write(str(g)) 
			f1.write('\n')
			f1.close()
			
		# feature8
		for index, obj in enumerate(sub8):
			if index != 129 and sub8[index]=='T' and sub8[index+1]=='A':
				ta += 1
		
		with open("feature8.txt", "a") as f1:
			f1.write(str(ta)) 
			f1.write('\n')
			f1.close()
			
		# feature9
		for index, obj in enumerate(sub9):
			if index != 129 and sub9[index]=='C' and sub9[index+1]=='C':
				cc += 1
		
		with open("feature9.txt", "a") as f1:
			f1.write(str(cc)) 
			f1.write('\n')
			f1.close()
			
		# feature10
		for index, obj in enumerate(sub10):
			if index != 129 and sub10[index]=='A' and sub10[index+1]=='T':
				at += 1
		
		with open("feature10.txt", "a") as f1:
			f1.write(str(at)) 
			f1.write('\n')
			f1.close()
			
		# feature11
		for index, obj in enumerate(sub11):
			if index != 129 and sub11[index]=='T' and sub11[index+1]=='T':
				tt += 1
		
		with open("feature11.txt", "a") as f1:
			f1.write(str(tt)) 
			f1.write('\n')
			f1.close()
			
		# feature12
		for index, obj in enumerate(sub12):
			if index != 129 and sub12[index]=='T' and sub12[index+1]=='C':
				tc += 1
		
		with open("feature12.txt", "a") as f1:
			f1.write(str(tc)) 
			f1.write('\n')
			f1.close()
	
	
	f1.close()


				
				
features("pos-train.txt")
