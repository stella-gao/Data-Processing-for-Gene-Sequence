def cdna(fasta_file):
    seq = ''
    header = ''

    for line in open(fasta_file):
        if line[0] == '>' :
            if seq:
                #print header
                with open("c_elegans_cdna.fa", "a") as f1:
                    f1.write(header)
                    f1.write('\n')
                    f1.write(seq)
                    f1.write('\n')
                header = ''
                seq = ''

            header = line.rstrip()

        else:
            if header:
                seq += line.rstrip()

    if seq:
        #print header
        with open("c_elegans_cdna.fa", "a") as f1:
            f1.write(header)
            f1.write('\n')
            f1.write(seq)
            f1.write('\n')
         
          
    f1.close()
        
                
             
    f = open("c_elegans_cdna.fa", "r")
    #lines = f.readlines() 
    
    f2 = open("c_elegans.mRNA.fa", "w") 

    
    for line in f: 
        if line[0] == '>':
            if line.split()[4] == "gene_biotype:protein_coding" and line.split()[5] == "transcript_biotype:protein_coding":
                f2.write(line)
                f2.write(next(f))

    f.close()
    f2.close()



cdna('Caenorhabditis_elegans.WBcel235.cdna.all.fa')
