str3 = "Shrutik.aaa"
str2 = "Lokare"
str1 = "Shrutika Dilip Lokare"

print(str1[0])                   #to print S

print(str1 + str2)               #to add two strings

print(str1[0:5])                 #slicing

print(str3 in str1)              #to check if str 3 is present in str1

str4 = "   white   "
print(str4.strip())              #to strip spaces
print(str4.lstrip())             #to strip left spaces
print(str4.rstrip())             #to strip right spaces

str3.split(".")                  #to split the string from the dot .
print(str3.split("."))           #print the splitted string
var = (str3.split("."))          #putting it in a list
print(var[0])                    #printing oth index of the list

