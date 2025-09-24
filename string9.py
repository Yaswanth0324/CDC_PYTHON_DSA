def word_mix(s1,s2):
    s3=s1[0:]+s2[:-1]
    return s3
st1=input("enter a string1: ")
str2=input("enter a string2: ")
res_parts = []
m = min(len(st1), len(str2))
for i in range(m):
    res_parts.append(st1[i])
    res_parts.append(str2[-1 - i])
if len(st1) > m:
    res_parts.append(st1[m:])
if len(str2) > m:
    res_parts.append(str2[:len(str2) - m])
print(''.join(res_parts))