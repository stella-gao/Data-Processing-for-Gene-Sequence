def add_head(output_file):
	f = open(output_file, "r")
    lines = f.readlines()
    f.close()
    f = open("train_false.txt", "w")
	cnt = 0
    for line in lines:
		cnt += 1 
        if cnt<=500 :
            f.write("> false-sample-header " + str(cnt) + "\n")
			f.write(line)
		elif cnt<=2100: 
			f.write(line)
		else:
			f.write("> false-sample-header \n")
			f.write(line)

    f.close()
	
add_head("train_false_1600.txt")
