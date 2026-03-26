#Question 1
#Write a Python program to find the largest of two numbers entered by the user.
'''
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))

if a>b:
    print("Largest number is: ",a)
elif a<b:
    print("Largest number is: ",b)
else:
    print("Both numbers are equal.")

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
    
#Question 3
#Finding maximum of three numbers

x=float(input("Enter the first number: "))
y=float(input("Enter the second number: "))
z=float(input("Enter the third number: "))
if x>y:
    if x>z:
        print("The largest number is: ",x)
    else:
        print("The largest number is: ",z)
else:
    if y>z:
        print("The largest number is: ",y)
    else:
        print("The largest number is: ",z)
'''

#When the student enters the marks, provide the grades based on the following criteria with nested if statements: 
'''
marks=float(input("Enter the marks: "))
if marks>=75:
    print("Grade: A")
else:
    if marks>=65:
        print("Grade: B")
    else:
        if marks>=55:
            print("Grade: C")
        else:
            if marks>=40:
                print("Grade: D")
            else:
                print("Grade: F")
'''

#using elif statements
'''
marks=float(input("Enter the marks: "))
if marks>=75:
    print("Grade: A")
elif marks>=65:
    print("Grade: B")
elif marks>=55:
    print("Grade: C")
elif marks>=40:
    print("Grade: D")
else:
    print("Grade: F")
'''

#Question 5
#Write a program to calculate the electricity bill of a house when consumed units according to the following criteria. 

'''
units=float(input("Enter the number of units consumed: "))
if units<=50:
    bill=units*10 
elif units<=90:
    bill=50*10 + (units-50)*15
else:
    bill=50*10 + 40*15 + (units-90)*50
print("Electricity bill is: ",bill + 1000)
'''

#Assessment 1

units = int(input("Enter the number of units consumed: "))
if units<=30:
    bill=units*5+500
elif units<=60:
    bill=(30*5)+((units-30)*10)+500
elif units<=100:
    bill=(30*5)+(30*10)+((units-60)*15)+500
else:
    bill =(30*5)+(30*10)+(40*15)+((units-100)*50)+500
print("electricity bill is : ", bill)