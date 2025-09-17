def new_string(s):
    first=s[0]
    mid=s[len(s)//2]
    last=s[-1]
    return first+mid+last
str1=input("enter a word: ")
print(new_string(str1))
