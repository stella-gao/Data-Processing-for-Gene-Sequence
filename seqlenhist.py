import numpy as np
import matplotlib.pyplot as plt

import plotly.plotly as py
# s = [1,1,1,1,2,2,2,3,3,4,5,5,5,6,7,7,7,7,7,7,7]

def len_hist(fasta_file):
	
	seq = ''
	header = ''
	seqlenvec = []
	for line in open(fasta_file):
		if line[0] == '>':			
			if seq:		
				seqlenvec.append(len(seq))
				header = ''
				seq = ''
							
			header = line.rstrip()
						
		else:
			seq += line.rstrip()			
		
	if seq:
		if seq:		
			seqlenvec.append(len(seq))

	
	return seqlenvec
	
	
s = len_hist("mRNA.fa")

'''
xmin = 0
xmax = 120000
step = 10000
y, x = np.histogram(s, bins=np.linspace(xmin, xmax, (xmax-xmin)/step))

nbins = y.size

plt.bar(x[:-1], y, width=x[1]-x[0], color='red', alpha=0.5)

plt.hist(s, bins=nbins, alpha=0.5)

plt.grid(True)
plt.show()
'''

print s

with open("mRNAseqlen.txt", "w") as f1:
	for item in s:
		f1.write("%s\n" % item)
					
#plt.hist(s)
#plt.show()

#fig = plt.gcf()

