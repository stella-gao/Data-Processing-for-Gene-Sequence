#!/usr/bin/env python
'''---------------------------------------------------------------------------------------
Make Hexamer frequency table
------------------------------------------------------------------------------------------'''

import os,sys
import string
from optparse import OptionParser
import warnings
import string
from collections import OrderedDict
from cpmodule.FrameKmer import kmer_freq_file
__author__ = "Liguo Wang"
__contributor__="Liguo Wang, Hyun Jung Park, Wei Li"
__copyright__ = "Copyright 2012, Mayo Clinic"
__credits__ = []
__license__ = "GPL"
__version__="1.2.2"
__maintainer__ = "Liguo Wang"
__email__ = "wang.liguo@mayo.edu;wangliguo78@gmail.com"
__status__ = "Production"

def main():
	usage = "\n%prog  [options]"
	parser = OptionParser(usage,version="%prog " + __version__)
	parser.add_option("-f","--cod",action="store",dest="coding_file",help="sequence in fasta format")
	(options,args)=parser.parse_args()

	if not options.coding_file:
		parser.print_help()
		sys.exit(0)		
	cod = kmer_freq_file(fastafile = options.coding_file, word_size = 6, step_size = 1, frame = 0)
	
	cod_sum = 0.0
	cod_sum += sum(cod.values())

	cod_sorted = sorted(cod, key=cod.get, reverse=True)
	
	with open("nue_hexamer.txt", "a") as f: 
		f.write('hexamer' + '\t' + 'coding' + '\n')
		for kmer in cod_sorted:
			if 'N' in kmer:
				continue
			with open("nue_hexamer.txt", "a") as f1: 
				f1.write(kmer + '\t' + str(float(cod[kmer]/cod_sum)) + '\n')



if __name__ == '__main__':
	main()
