a = int(input())
b = int(input())
c = int(input())
if a<b:
    a,b=b,a
if a<c:
    a,c=c,a
if b<c:
    b,c=c,b
if a>=b>c:
    print("1")
elif a>b:
    print("2")
else:
    print("0")
