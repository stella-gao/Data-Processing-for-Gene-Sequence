from __future__ import division
import numpy as np

from sklearn.metrics import roc_curve, auc, roc_auc_score
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import accuracy_score


def prob(output_file):
    
    f = open(output_file, "r")    
    lines = f.readlines()
    f.close()
    
    f = open(output_file,"w")
    for line in lines:
        if line.split()[0]!= 'Transcript_id':
            f.write(line)
    
    f.close() 

    count = 0
    for line in open(output_file):
        count += 1
        print line
       
    print count
    
    cnt = 0

    outFile = open("mi.txt", "w")
    outFile.write('mi')
    outFile.write('\n')
    for line in open(output_file):
        cnt += 1
        y_predict.append(float(line.split()[2]))
        print float(line.split()[2])
        outFile.write(line.split()[2])
        outFile.write('\n')
        
prob("human02.new")
