#1
age=int(input("please enter your age:"))
money=int(input("please enter your money:"))
tkt_cost=15
if age>=12 and money>=tkt_cost:
    print("Enjoy the movie")
else:
    print("Access denied")


#2
year = int(input("please enter your year:"))
if (year%4 and year != 100) or year/400:
    print("leap year")
else:
    print("not leap year")


#3
pin_code = int(input("please enter your pin:"))
amount=int(input("please enter your money:"))
pin=1234
balance=500

if pin_code==pin:
    if amount<=0:
        print("Invalid amound")
    elif amount>balance:
        print("Not enough money")
    else:
       balance = balance -amount
       print(f'take your money:{amount}')
       print(f"new balance:{balance}")
else:
       print("wrong pin")


#4
try:
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    number = int(input('Enter a number to divide 100 by: '))

    print('100 /', number, '=', 100 / number)
    print(f'Hello, ' + {name} + '! Next year you will be ' + {age + 1} + ' years old.')
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("cannot divide by zero")
except TypeError:
    print("cannot join text and number")
except exception as e:
    print(e)












