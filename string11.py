from collections import Counter
def char_freq(s):
    freq=Counter(s)
    return freq
str1=input("enter a string: ")
print("character frequency: ",char_freq(str1))