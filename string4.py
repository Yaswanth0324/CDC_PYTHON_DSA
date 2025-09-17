def string(s1,s2):
    mid1=len(s1)//2
    mid2=len(s2)//2
    s3=s1[0]+s2[0]+s1[mid1]+s2[mid2]+s1[-1]+s2[-1]
    return s3
str1=input("enter a string1:")
str2=input("enter a string2:")
print(string(str1,str2))