#1
number = int(input("Enter the odd number:"))
if number % 2 ==0:
    print("even number")
else:
    print("odd number")


#2

age = int(input("Enter your age:"))
if age <0:
    print("Invalid age")
elif age <=12:
    print("child")
elif age <=17:
    print("teenager")
elif age <=64:
    print("Adult")
else :
    print('Senior')

#3
grade = int(input("Enter your grade:"))

if grade <0 or grade >100:
    print("Invalid grade")
elif grade >=90:
    print("A")
elif grade >=80:
    print("B")
elif grade >=70:
    print("C")
elif grade >=60:
    print("D")
elif grade >=50:
    print("E")
else :
    print("F")


#4
answer = input("Do you like python:").strip().lower()

if answer == "yes":
    print("Great!")
elif answer == "no":
    print("Maybe you will like it later")
else:
    print("Please enter yes or no")


#5
first_number = float(input("Enter the first number:"))
operation = input("Enter the operation")
second_number = float(input("Enter the second number:"))

if operation == "+":
    print (first_number + second_number)
elif operation == "-":
    print (first_number - second_number)
elif operation == "*":
    print (first_number * second_number)
elif operation == "/":
    print (first_number / second_number)
else:
    print("unknown operation")
















