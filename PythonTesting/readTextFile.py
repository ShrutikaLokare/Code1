file = open("text.txt")   #to open the text file

#print(file.read())        #to print all the content of the file

#print(file.read(4))       #to read upto 4 value

#print(file.readline())     #to read the first line

#print(file.readline())     #to read the second line
#file.close()              #to close the file

#when we have 100 lines, we just can't write file.readline 00 times, we need to use the logic using for loop
#print all the data line by line present in the file

#line = file.readline()
#first method using while loop
while line != "":
    print(line)
    line = file.readline()

print(file.readlines())            #to create list of all line, each line in one index


#second method using readlines()
for line in file.readlines():
    print(line)
file.close()