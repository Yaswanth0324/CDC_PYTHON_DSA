def word_balance(s1, s2):
    # Return True if every character in s1 appears in s2 (position doesn't matter)
    return all(ch in s2 for ch in s1)

str1 = input("enter a string1: ")
str2 = input("enter a string2: ")
print(word_balance(str1, str2))