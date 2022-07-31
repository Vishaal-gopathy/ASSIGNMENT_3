def reverse(string):
    str = ""
    for i in string:
        str = i + str
    return str
 
string = "1234abcd"
 
print("The original string is : ", end="")
print(string)
 
print("The reversed string is : ", end="")
print(reverse(string))