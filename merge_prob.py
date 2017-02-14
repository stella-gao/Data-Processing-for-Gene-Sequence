from __future__ import division
import numpy as np
import sys

#from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc, roc_auc_score
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import accuracy_score

'''
est = LogisticRegression(class_weight='auto')
X = np.random.rand(10, 2)
y = np.random.randint(2, size=10)
est.fit(X, y)
'''


def merge(outfile1, outfile2, outfile3, outfile4, outfile5):

    f1 = open(outfile1, "r")
    f2 = open(outfile2, "r")
    f3 = open(outfile3, "r")
    f4 = open(outfile4, "r")
    f5 = open(outfile5, "r")
    lines1 = f1.read().splitlines()
    lines2 = f2.read().splitlines()
    lines3 = f3.read().splitlines()
    lines4 = f4.read().splitlines()
    lines5 = f5.read().splitlines()
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    
    f = open("merge2.txt","w")
    for i in range(1,10810):
        f.write(lines1[i]+' ')
        f.write(lines2[i]+' ')
        f.write(lines3[i]+' ')
        f.write(lines4[i]+' ')
        f.write(lines5[i]+' ')
        lines1[i] = float(lines1[i])
        lines2[i] = float(lines2[i])
        lines3[i] = float(lines3[i])
        lines4[i] = float(lines4[i])
        lines5[i] = float(lines5[i])
        if (lines1[i]> lines2[i] and lines1[i]>lines3[i] and lines1[i]> lines4[i] and lines1[i]> lines5[i]):
            f.write('pc\n')
        if (lines2[i]>lines1[i] and lines2[i]> lines3[i] and lines2[i]> lines4[i] and lines2[i]> lines5[i]):
            f.write('lnc\n')
        if (lines3[i]>lines1[i] and lines3[i]> lines2[i] and lines3[i]> lines4[i] and lines3[i]> lines5[i]):
            f.write('mi\n')
        if (lines4[i]>lines1[i] and lines4[i]> lines2[i] and lines4[i]> lines3[i] and lines4[i]> lines5[i]):
            f.write('sn\n')
        if (lines5[i]>lines1[i] and lines5[i]> lines2[i] and lines5[i]> lines3[i] and lines5[i]> lines4[i]):
            f.write('sno\n')


    f.close()
    
    
    merge('pc.txt', 'lnc.txt', 'mi.txt', 'sn.txt','sno.txt')
