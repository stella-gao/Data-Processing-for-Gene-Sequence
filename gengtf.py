def generate_gtf(fasta_file):
	id = ''
	exon = ''
	for line in open(fasta_file):
		if line[0] == '>':
			line = line.strip()
			id = line.split(">",1)[1]
			exon = line.split(":",1)[1]
			w1 = 'chr1	HAVANA	exon	' + exon.split('-',1)[0] + ' ' + exon.split('-',1)[1] + '	.	+	.	'  
			w2 = 'gene_id ' + '"' + id + '"' + '; transcript_id ' + '"' + id + '"'+';'
			with open("train.gtf", "a") as f1:
				f1.write(str(w1)+str(w2))
				f1.write('\n')
				
	f1.close()
		
		
		
		
generate_gtf('m6A.tv.all.fa')
