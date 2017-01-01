################################################################################
# merge-data-random-test  by Stella Gao
#
# Input
#  fasta_file:  Input FASTA file.
#
# Output
#  2 files:    pos.fa, neg.fa
################################################################################

import random
from collections import OrderedDict

def split_pos_neg_fa(fasta_file):
	
	#count the number of samples
	count = 0
	for line in open(fasta_file):
		if line[0] == '>':
			count += 1
			
	print count
	
	posSplit = int(count*0.6)
	#negSplit = int(trainSplit + count*0.1)

	# load and code sequences
	seq_vecs = OrderedDict()
	seq = ''
	for line in open(fasta_file):
		if line[0] == '>':
			if seq:
				seq_vecs[header] = seq
			#
			header = line.rstrip()
			seq = ''
		else:
			seq += line.rstrip()
	#
	if seq:
		seq_vecs[header] = seq
	
	
	items = seq_vecs.items()
	random.shuffle(items)
	dict = OrderedDict(items)
	
	i = 0
	for header in dict.keys():
		i += 1
		if i <= trainSplit:
			with open("pos.fa", "a") as ftrain:				
				ftrain.write(header) 
				ftrain.write('\n')
				ftrain.write(dict[header])
				ftrain.write('\n')
		else:
			with open("neg.fa", "a") as ftest:				
				ftest.write(header) 
				ftest.write('\n')
				ftest.write(dict[header])
				ftest.write('\n')
		
		
split_pos_neg_fa("Data.fa")
