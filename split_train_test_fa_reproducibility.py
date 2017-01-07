################################################################################
# split_train_test_fa  by Stella Gao
#
# Input
#  fasta_file:  Input FASTA file.
#
# Output
#  3 files:    train.fa, test.fa, valid.fa
################################################################################

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

    trainSplit = int(count*0.8)
    testSplit = int(trainSplit + count*0.1)

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
        if i <= trainSplit:
            with open("CDS_train_rmspace.fa", "a") as ftrain:
                ftrain.write(header)
                ftrain.write('\n')
                ftrain.write(dict[header])
                ftrain.write('\n')
        elif i<=testSplit:
            with open("CDS_test_rmspace.fa", "a") as ftest:
                ftest.write(header)
                ftest.write('\n')
                ftest.write(dict[header])
                ftest.write('\n')
        else:
            with open("CDS_valid_rmspace.fa", "a") as fvalid:
                fvalid.write(header)
                fvalid.write('\n')
                fvalid.write(dict[header])
                fvalid.write('\n')


split_train_test_fa("cpat_CDS_rmspace.fa")
