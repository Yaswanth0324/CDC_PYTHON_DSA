from collections import Counter
a=[1,2,6,8,4,6,3]
print(a)
a.sort()
print(a)
a.append(10)
a.insert(3,15)
print(a)    
freq=Counter(a)
print(freq)
min_value = 5
for i in a:
    if i < min_value:
        min_value = i
print("minimum value is:", min_value)
print(len(a))
#concatination
b=[11,12,13]
c=a+b
print(c)