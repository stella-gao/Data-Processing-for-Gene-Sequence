import matplotlib
matplotlib.use('Agg')

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
    
    
s = len_hist("train2.mRNA.human.fa")



bins = np.linspace(0, 15000, num=150)

plt.hist(s, bins, alpha=0.5, label='x')

#y, x = np.histogram(s, bins=np.linspace(xmin, xmax, (xmax-xmin)/step))
#nbins = y.size
#plt.bar(x[:-1], y, width=x[1]-x[0], color='red', alpha=0.5)
#plt.hist(s, bins=nbins, alpha=0.5)
plt.grid(True)
plt.show()

plt.title('Sequence Length', size=14)
plt.xlabel('x-axis', size=14)
plt.ylabel('y-axis', size=14)
#plt.plot(xData, yData1, color='b', linestyle='--', marker='o', label='y1 data')
#plt.plot(xData, yData2, color='r', linestyle='-', label='y2 data')
#plt.legend(loc='upper left')
plt.savefig('mrna.png', format='png')


#print s

with open("train.mlen.txt", "w") as f1:
    for item in s:
        f1.write("%s\n" % item)
