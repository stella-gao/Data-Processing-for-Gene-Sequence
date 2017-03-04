from __future__ import division
import numpy as np

#from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc, roc_auc_score
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import accuracy_score


def error_rate(output_file):
    count = 0
    for line in open(output_file):
        count += 1
        print line

    print count

    cnt = 0
    error = 0
    y = []
    y_predict = []

    for line in open(output_file):
        cnt += 1
        print float(line.split()[4])
        y_predict.append(float(line.split()[4]))
        if cnt <= 48:
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

error_rate("tf.pac.txt")
