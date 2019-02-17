name=input("Enter your name")
print("Hello",name,'Enter the number for Table')
number=int(input("Enter number for table"))

if number == 0:
   print ("Do not enter 0")

elif number<0:
   print("Do not enter -ve number")
   

else:

    for i in range(1,11):
        table=number*i
        print(number,"*",i,'=',table)
