#if there is a failure in try then it will go to except block
#but whether the try block fails or not, cursor will definitely go to "finally"
#to customize error message if try fails

try:
    with open("texxxt.txt", "r") as reader:
     content = reader.readlines()
     print(content)

except:
    print("try block got failed")


#to get python original error message
try:
    with open("text.txt", "r") as reader:
     content = reader.readlines()
     print(content)

except Exception as b:
    print(b)

finally:
    print("cleaning up resources")