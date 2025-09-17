def mid_string(s):
    mid=len(s)//2
    return s[mid-1:mid+2]
str1=input("enter a string: ")
print(mid_string(str1))