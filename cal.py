a = int(input("enter your number"))
b = int(input("enter your number"))
# input = (input("enter op")).strip()
input = (input("enter op"))
if(input =='+'):
    print(a+b)
elif input=='-':
    print(a-b)
elif input=='*':
    print(a*b)
elif input=='%':
    print(a%b)
else:
    print("try again")


