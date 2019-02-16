fact=1
name=input("Enter your name-")

print('\n\nHello '+name,'Happy coading life')

number=int(input("enter number for factorial-"))

if number==0:
    
    print(name,"factorial of",number,"is 1")
    
elif number<0:
    
    
    print(name,"Do not enter (-ve) number")
    
else:
    for i in range(1,number+1):
        fact=fact*i
    print('\nFactorial of',number,'=',fact)
    
    print("\nDont take much stress coading is to easy:)")
        
