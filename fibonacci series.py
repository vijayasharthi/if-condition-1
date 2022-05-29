d=int(input("enter the number"))
a= 1
b=1
print(a, end = " ")
print(b,end = " ")
for i in range(d):
    c=a+b
    print(c, end="  ")
    a, b= b, c
