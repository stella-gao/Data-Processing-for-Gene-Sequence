from __future__ import division
import numpy as np

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


def error_rate(output_file):

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
    
    # flag = int(count/2) 
    flag = 8871
    print flag
    cnt = 0
    error = 0
    y = []
    y_predict = []
    for line in open(output_file):
        cnt += 1
       # print line.split()[1]    
#    for word in line.split():
    #        print word[1]
        y_predict.append(float(line.split()[2]))
        if cnt <= flag:
            y.append(1)
        else:
            y.append(0)

    y_predict = np.array(y_predict)
    y = np.array(y)
    print "y_predict"
    print y_predict
    print "y"
    print y
    false_positive_rate, true_positive_rate, thresholds = roc_curve(y, y_predict)
    print "AUC is :"
    print auc(false_positive_rate, true_positive_rate)
    print roc_auc_score(y, y_predict)
    print "--------------------------------------------"
    print "MCC is :"
    print matthews_corrcoef(y, [round(x) for x in y_predict])
    print "--------------------------------------------"
    print "Accuracy is :"
    print accuracy_score(y, [round(x) for x in y_predict])

    testRounded = [round(x) for x in y_predict]
    #print(testRounded)
    #print count

    cnt = 0
    for i in xrange(count):
        cnt += abs(testRounded[i] - y[i])

    error_rate = (cnt/count)*100

    print("Test error rate is: %.4f%%" % error_rate)
    print("Accuracy is: %.4f%%" % (100 - error_rate))

'''
        if line[0] == 'C' and cnt <= flag :
            error += 1
        if line[0] == 'N' and cnt > flag:
            error += 1
            
    print("Test error rate is: %.4f%%" % ((error/count)*100))
'''
error_rate("zebrafish.ret")
