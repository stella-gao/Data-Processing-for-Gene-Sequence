################################################################################
# Merge Pos and Neg Data  by Stella Gao
#
# Input
#  fasta_files:  Input two FASTA files.
#
# Output
#  1 file:    Output one FASTA files.
################################################################################


def merge_fa(fasta_file1, fasta_file2):
	for line in open(fasta_file2):
		with open(fasta_file1, "a") as f:				
			f.write(line) 



		
merge_fa("lnctrain.fa","mtrain.fa")
merge_fa("lnctest.fa","mtest.fa")
merge_fa("lncvalid.fa","mvalid.fa")
