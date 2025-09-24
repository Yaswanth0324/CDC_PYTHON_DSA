def num_pali(n):
    rev=int(str(n)[::-1])
    print(rev)
    if(n==rev):
        return True
    else:
        return False
num=int(input("enter a number: "))
print(num_pali(num))
