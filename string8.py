def rem_dup(s):
    s1=[]
    for char in s:
        if char not in s1:
            s1.append(char)
    return ''.join(s1)
str1=input("enter a string: ")
print("string after removing duplicates: ",rem_dup(str1))
