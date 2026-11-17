#1
import secrets

i=2
while i<=50:
    if i % 2 ==0:
        print(i)
    i +=1

#2
n=int(input("enter the number:"))
i=1
total=0

while i<=n:
    total+=i
    i+=1
print(f"sum:{total}")

#3
n=int(input("enter the number:"))
while n<0:
    n=int(input("enter the number:"))
factorial=1
i=1
while i<=n:
    factorial*=i
    i+=1
print(f"n!={factorial}")

#4
count=0
total=0
number=int(input("enter the number:"))
while number !=0:
    count+=1
    total+=number
    number=int(input("enter the number:"))
print("count:",count)
print("total:",total)
if count>0:
    average=total/count
    print(f"average:{average}")


#5
secret=7
tries=0
guess=0
while tries<5 and guess!=secret:
    guess=int(input("enter the guess:"))
    tries+=1
    if guess>secret:
        print("too high")
    elif guess<secret:
        print("too low")
    else:
        print("you win")
if guess!=secret:
    print("you lose! the number was 7")








