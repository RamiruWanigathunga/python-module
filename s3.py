a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))

if a>b:
    print("Largest number is: ",a)
elif a<b:
    print("Largest number is: ",b)
elif a==b:
    print("Both numbers are equal.")
else:    
    print("Invalid input.")