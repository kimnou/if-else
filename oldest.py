a=int(input("enter the age"))
b=int(input("enter the age"))
c=int(input("enter the age"))
if a>b and a>c:
    print("a is oldest")
elif a<b and a<c:
    print("a is youngest")
elif b>a and b>c:
    print("b is oldest")
elif b<a and b<c:
    print("b is youngest")
elif c>a and c>b:
    print("c is oldest")
else:
    print("c is youngest")
