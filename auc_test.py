from __future__ import division
import numpy as np

#from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc, roc_auc_score


#y = []
#y_predict = []

def error_rate(output_file):

    #count the number of samples
    count = 0
    for line in open(output_file):
            count += 1

    print count

    flag = count/2
    cnt = 0
    error = 0
    y = []
    y_predict = []
    for line in open(output_file):
        cnt += 1
       # print line.split()[1]
#    for word in line.split():
    #        print word[1]
        y_predict.append(float(line.split()[1]))
        if cnt <= flag:
            y.append([-1])
        else:
            y.append([1])

    y_predict = np.array(y_predict)
    y = np.array(y)
    print "y_predict"
    print y_predict
    print "y"
    print y
    false_positive_rate, true_positive_rate, thresholds = roc_curve(y, y_predict)
    print auc(false_positive_rate, true_positive_rate)
    print roc_auc_score(y, y_predict)

error_rate("PLEKsample1129.predicted")


