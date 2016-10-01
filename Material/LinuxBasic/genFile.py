import random
random.seed(1)
f = open("largeFile.txt", 'w')
for i in range(1000000):
	f.write(str(random.randint(0,10000))+'\n')
f.close()
f = open("helloCat.txt", "w")
f.write("Ya!!! You know how to use cat\n")
f.close()
