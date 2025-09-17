def Palindrome(a):
    a=input("enter a string: ")
    temp =a
    b=a[::-1]
    if(temp==b):
        print(temp,"is a palindrome")
    else:
        print(temp,"is not a palindrome")
Palindrome("")