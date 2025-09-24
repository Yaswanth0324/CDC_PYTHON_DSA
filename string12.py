from collections import Counter
def firstUniqChar(s):
    freq = Counter(s)
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1
s1 = input("enter a string: ")
print(firstUniqChar(s1))
