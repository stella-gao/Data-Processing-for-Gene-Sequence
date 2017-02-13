print y_train1
binarizer = MultiLabelBinarizer().fit(y_train1)
y_train = binarizer.transform(y_train1)
print y_train
print binarizer.inverse_transform(y_train)
