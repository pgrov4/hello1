print("Q.1- Write a Python program to read last n lines of a file")
f=open("test.txt",'r')
lines=f.readlines()
#print(lines)
position=f.tell()
print(position)
f.seek(0)
print("no of lines",len(lines))
len1=len(lines)
print("no of lines",len1)
n=int(input("enter the no of lines you want to print from the last"))
x=len1-(len1-3)
#print(x)
#f.seek(lines[x],0)
i=0
for i in range(0,len1):
    if(i>=x):
        print(f.readline())
    else:
        f.readline()
    #i=i+1
#print(line)
print("Q.2- Write a Python program to count the frequency of words in a file.")
file=open("test.txt",'r')

wordcount={}

for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k,v in wordcount.items():
    print(k, v)


print("Q.3- Write a Python program to copy the contents of a file to another file")
f = open('test.txt')
f1 = open('output.txt', 'a')

doIHaveToCopyTheLine=False

for line in f.readlines():
    f1.write(line)

f1.close()
f2=open('output.txt','r')
print(f2.readlines())
f.close()


print("Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.")
with open('test.txt') as fh1, open('read.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        # line1 from abc.txt, line2 from test.txtg
        print(line1+line2)


print("Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.")
import random
afile = open("Random.txt", "w" )

for i in range(int(input('How many random numbers?: '))):
    line = str(random.randint(1, 100))
    afile.write(line)
    print(line)
afile.close()

