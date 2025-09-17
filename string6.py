def str_count(s):
    chars=0
    digits=0
    symbols=0
    for char in s:
        if char.isalpha():
            chars+=1
        elif char.isdigit():
            digits+=1
        else:
            symbols+=1
    return chars ,digits,symbols
str1=input("enter a string: ")
chars, digits, symbols = str_count(str1)
print("characters: ",chars)
print("digits: ",digits)
print("symbols:",symbols)