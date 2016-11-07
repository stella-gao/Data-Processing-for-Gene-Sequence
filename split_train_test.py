# method 1  Reference: https://github.com/ruhan/toyslim/blob/9b69f17c56e6eec54ffc4273c78ae44d4f292271/util.py
def split_train_test(file_tsv):
    """
    Split a tsv file into two others:
        1) Train file with 80 perc of the data
        2) Test file with 20 perc of the data
    """
    M = tsv_to_matrix(file_tsv)

    m, _ = M.shape

    train_list = []
    test_list = []

    for i in range(m):
        data = M[i].nonzero()[1]
        random.shuffle(data)

        # 80%
        mark = int(len(data) * 0.8)

        train = data[:mark]
        test = data[mark:]

        train_list.append(train)
        test_list.append(test)

    def store_matrix(data_list, ofile):
        result = []
        for i, data in enumerate(data_list):
            for d in data:
                result.append('%s %s %s' % (i, d, '1.0'))
        result = "\n".join(result)

        f = open(ofile, 'w')
        f.write(result)
        f.close()

    file_without_ext = file_tsv.rsplit('.', 1)[0]
    file_train = '%s_train.tsv' % file_without_ext
    file_test = '%s_test.tsv' % file_without_ext

    store_matrix(train_list, file_train)
    store_matrix(test_list, file_test)
    mark = int(len(data) * 0.8)

    return file_train, file_test


  
import sys
split_train_test(sys.argv[1])

# method 2
def split_train_validation_test(file_tsv):
    """
    Split a tsv file into two others:
        1) Train file with 80 perc of the data
        2) Test file with 20 perc of the data
    """
    M = tsv_to_matrix(file_tsv)

    m, _ = M.shape

    train_list = []
    validation_list = []
    test_list = []

    for i in range(m):
        data = M[i].nonzero()[1]
        random.shuffle(data)

        # 60%
        mark_train = int(len(data) * 0.6)

        # 20%-20%
        train = data[:mark_train]
        other = data[mark_train:]

        mark_validation = int(len(other) * 0.5)
        validation = other[:mark_validation]
        test = other[mark_validation:]

        train_list.append(train)
        validation_list.append(validation)
        test_list.append(test)

    # TODO: remove this duplication =/
    def store_matrix(data_list, ofile):
        result = []
        for i, data in enumerate(data_list):
            for d in data:
                result.append('%s %s %s' % (i, d, '1.0'))
        result = "\n".join(result)

        f = open(ofile, 'w')
        f.write(result)
        f.close()

    file_without_ext = file_tsv.rsplit('.', 1)[0]
    file_train = '%s_train.tsv' % file_without_ext
    file_validation = '%s_validation.tsv' % file_without_ext
    file_test = '%s_test.tsv' % file_without_ext

    store_matrix(train_list, file_train)
    store_matrix(validation_list, file_validation)
    store_matrix(test_list, file_test)

    return file_train, file_validation, file_test
  
  
import sys
split_train_validation_test(sys.argv[1])


# Method 3

rows = open("datafile", "r").read().split('\n')

count = len(rows)
trainSplit = int(count*0.6)
testSplit = int(trainSplit + count*0.2 )

train = open("datafile" + ".train", "w+")
test = open("datafile" + ".test","w+")
val = open("datafile" + ".val","w+")


for i in range(0, trainSplit):
	train.write(rows[i] + "\n")
	
for i in range(trainSplit,testSplit):
	test.write(rows[i] + "\n")

for i in range(testSplit,count):
	val.write(rows[i] + "\n")


  
# Method 4  Reference: https://github.com/manas15/data-mining/tree/67ced5991dff38ba5900e15f18dc8ab849f41eb8
import random
def splitDataset(dataset, splitRatio):
	trainSize = int(len(dataset) * splitRatio)
	trainSet = []
	copy = list(dataset)
	while len(trainSet) < trainSize:
		index = random.randrange(len(copy))
		trainSet.append(copy.pop(index))
	return [trainSet, copy]

dataset = [[1], [2], [3], [4], [5]]
splitRatio = 0.67
train, test = splitDataset(dataset, splitRatio)
print('Split {0} rows into train with {1} and test with {2}').format(len(dataset), train, test)

