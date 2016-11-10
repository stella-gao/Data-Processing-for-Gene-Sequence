from __future__ import division

def error_rate(output_file):

    #count the number of samples
    count = 0
    for line in open(output_file):
            count += 1

    print count

    flag = count/2
    cnt = 0
    error = 0
    for line in open(output_file):
        cnt += 1
        if line[0] == 'C' and cnt <= flag :
            error += 1
        if line[0] == 'N' and cnt > flag:
            error += 1

    print("Test error rate is: %.3f%%" % ((error/count)*100))


error_rate("20161109.predicted")
