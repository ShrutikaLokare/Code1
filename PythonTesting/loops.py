rollno = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in rollno:
    print(i)
    print(i*2)

#SUMMATION OF FIRST 10 NUMBERS

addition = 0
for j in range(1, 11):   #range(i, j)means i to j-1
    addition = addition + j
    print(j)
print(addition)

#for  third index (to iterate n times)

for s in range(1, 10, 2):
    print(s)
print("*******************")

#skipping first index

for a in range(10): #first index will be considered as 0 always and not 1
    print(a)

print("Second commit")