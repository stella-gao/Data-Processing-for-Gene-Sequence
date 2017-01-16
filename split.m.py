import random
from collections import OrderedDict
import numpy as np
import h5py
import scipy.io
np.random.seed(1337) # for reproducibility


def split_train_test_fa(fasta_file):

    #count the number of samples
    count = 0
    for line in open(fasta_file):
        if line[0] == '>':
            count += 1

    print count

    Split01 = int(count*0.1)
    Split02 = int(count*0.2)
    Split03 = int(count*0.3)
    Split04 = int(count*0.4)
    Split05 = int(count*0.5)
    Split06 = int(count*0.6)
    Split07 = int(count*0.7)
    Split08 = int(count*0.8)
    Split09 = int(count*0.9)

   # testSplit = int(trainSplit + count*0.1)

    # load and code sequences
    seq_vecs = OrderedDict()
    seq = ''
    for line in open(fasta_file):
        if line[0] == '>':
            if seq:
                seq_vecs[header] = seq
            #
            header = line.rstrip()
            seq = ''
        else:
            seq += line.rstrip()
    #
    if seq:
        seq_vecs[header] = seq


    items = seq_vecs.items()
    np.random.shuffle(items)
    dict = OrderedDict(items)

    i = 0
    for header in dict.keys():
        i += 1
        if i <= Split01:
            with open("mRNA.rat.01.fa", "a") as f1:
                f1.write(header)
                f1.write('\n')
                f1.write(dict[header])
                f1.write('\n')
        elif i <= Split02:
            with open("mRNA.rat.02.fa", "a") as f2:
                f2.write(header)
                f2.write('\n')
                f2.write(dict[header])
                f2.write('\n')
        elif i <= Split03:
            with open("mRNA.rat.03.fa", "a") as f3:
                f3.write(header)
                f3.write('\n')
                f3.write(dict[header])
                f3.write('\n')
        elif i <= Split04:
            with open("mRNA.rat.04.fa", "a") as f4:
                f4.write(header)
                f4.write('\n')
                f4.write(dict[header])
                f4.write('\n')
        elif i <= Split05:
            with open("mRNA.rat.05.fa", "a") as f5:
                f5.write(header)
                f5.write('\n')
                f5.write(dict[header])
                f5.write('\n')
        elif i <= Split06:
            with open("mRNA.rat.06.fa", "a") as f6:
                f6.write(header)
                f6.write('\n')
                f6.write(dict[header])
                f6.write('\n')
        elif i <= Split07:
            with open("mRNA.rat.07.fa", "a") as f7:
                f7.write(header)
                f7.write('\n')
                f7.write(dict[header])
                f7.write('\n')
        elif i <= Split08:
            with open("mRNA.rat.08.fa", "a") as f8:
                f8.write(header)
                f8.write('\n')
                f8.write(dict[header])
                f8.write('\n')
        elif i <= Split09:
            with open("mRNA.rat.09.fa", "a") as f9:
                f9.write(header)
                f9.write('\n')
                f9.write(dict[header])
                f9.write('\n')
        else:
            with open("mRNA.rat.10.fa", "a") as ftest:
                ftest.write(header)
                ftest.write('\n')
                ftest.write(dict[header])
                ftest.write('\n')


split_train_test_fa("rat.mRNA.fa")
