#Question 1
#Write a Python program to find the largest of two numbers entered by the user.
'''
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
'''
#Question 2
#Write a Python program to check a person is eligible to vote or not.

age=input("Enter your age: ")
if age.isdigit():
    age=int(age)
    if age>=18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
else:
    print("Invalid input. Please enter a valid age.")