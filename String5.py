def string(s):
    s1=[]
    s2=[]
    for char in s:
        if char.islower():
            s1.append(char)
        else:
            s2.append(char)
    return "".join(s1+s2)
str1=input("enter a string: ")
print(string(str1))