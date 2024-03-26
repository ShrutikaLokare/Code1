values = [1, 2, 5.5 ,"hello", 10+5j]

#to print the values
print(values[0]) #1
print(values[2]) #5.5
print(values[3]) #hello
print(values[4]) #10+5j
print(values[-1]) #10+5j

#to print multiple values
print(values[1:4])
print(values[0:1])

#to insert additional value
values.insert(3, "shrutika")

#to print values list with additional value
print(values)

#to append the values
values.append("aditya")
print(values)

#to change the value
values[3] = "SHRUTIKA"
print(values)

#to delete the values
del values[0:3]
print(values)