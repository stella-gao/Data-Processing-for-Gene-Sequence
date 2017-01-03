from __future__ import division
import numpy as np


from sklearn.metrics import roc_curve, auc, roc_auc_score



def acc(output_file):
    
    f = open(output_file, "r")    
    lines = f.readlines()
    f.close()
    f = open(output_file,"w")
    for line in lines:
        if line[0]!= 'T':
            f.write(line)
    
    f.close() 
#count the number of samples
    count = 0
    for line in open(output_file):
        count += 1
        print line
            
    print count
    
    flag = 1776 
    cnt1 = 0
    cnt2 = 0
    print flag
    cnt = 0
	
    for line in open(output_file):
        cnt += 1
        # y_predict.append(float(line.split()[2]))
        if cnt <= flag and line.split()[1] == "noncoding":
            cnt1 += 1
        if cnt > flag and line.split()[1] == "coding":
            cnt2 += 1

	
    print cnt1
    error1 = cnt1/1776
    print error1
    
    
    print cnt2
    error2 = cnt2/(count-1776)
    print error2
    
    total = cnt1 + cnt2
    print total
    print total/count
    print 1-total/count



acc("haha")

