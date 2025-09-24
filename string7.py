def rem_vowel(s):
    for char in s:
        if char in 'aeiouAEIOU':
            s = s.replace(char, '')
    return s
str1=input("Enter a string: ")
print("String after removing vowels:",rem_vowel(str1))