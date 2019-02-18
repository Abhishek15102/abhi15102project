print("Be happy\nWork hard and eat healthy food")

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def modu(a,b):
    return a%b
name=input("Enter your name-->")
print("insert operation")
print("Addition (+)")
print("Substraction (-)")
print("multiplication(*)")
print("division(/)")
print("modulo(%)")

sign=input("insert operation here->")
first=float(input("Enter 1st number--->"))
second=float(input("enter 2nd number-->"))

if sign=='+':
    print(add(first,second))
elif sign=='-':
    print(sub(first,second))
elif sign=='*':
    print(mul(first,second))
elif sign=='/':
    print(div(first,second))
elif sign=='%':
    print(modu(first,second))
else:
    print(name,"please Enter valid operation")
    
    
print("Happy coading")

print("please run code again (f5)")
