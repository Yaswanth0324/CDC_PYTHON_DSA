name="yash"
print(name)
print(name[1])
for x in name:
    print(x)
print(len(name))
print("a" in name)
if "a" in name:
    print("yes")
elif "a" not in name:
    print("no")
else:
    print("nothing")
print(name[0:3])
print(name[-4:-1])
print(name.upper())
word="  pushpa raj  "
print(word.strip())
print(word.replace("P","P"))
print(word.split(","))
a="hello"
b="world"
c=a+b
print(c)
print(a+" "+b)
price=45
txt=f"the price of apple is {price} rupees"
print(txt)
txt1=f"the price of apple is {price:.2f} rupees"
print(txt1)
txt2 = f'the price of \"Mango\" is {price} rupees'
print(txt2)
print(txt1.capitalize())
print(txt1.upper())
print(txt1.lower())
print(txt1.count("a"))
print(txt1.find("is"))