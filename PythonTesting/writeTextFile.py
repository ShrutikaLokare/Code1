file = open("text.txt")  #to open the file
file.close()             #to close the file

#instead of 2 lines, there is a way where we do not need to close the file

#with open("text.txt", "r") as file:      #single line to open and close the file and saved the value in file as object#

#to open the file, reverse the file and write back in the file
with open("text.txt", "r") as reader: #to open the file, store the value in reader
    content = reader.readlines()      #readlines to create a list of the values from the file
    print(content)                    #printing the list
    rev = reversed(content)           #to reverse the list and store in rev
    with open("text.txt", "w") as writer:   #to open the file in write w mode and close the file
        for line in rev:                    #to write the reversed list in file
         writer.write(line)

