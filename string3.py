def mid_str(s1,s2):
    mid=len(s1)//2
    s3= s1[:mid]+s2+s1[mid:]
    return s3
str1=input("enter a string1:")
str2=input("enter a string2:")
print(mid_str(str1,str2))
