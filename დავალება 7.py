#1

for i in range (11):
    print(f"{i} squared = {i**2}")

for i in range (10,0,-1):
    print(i)
print("go!")

total=0
for i in range (2,101,2):
    total +=i
print(total)

#2
txt =input("enter your text").lower()
count=0
for i in txt:
    if i in "aeiou":
        count+=1
print("vowels:",count)

#3
total=0
count=0
while True:
    n=input("enter a number:")
    if n == "stop":
        break
    n=int(n)
    if n<0:
        print("negative numbers are not allowed")
        continue

    total+=n
    count+=1
print("sum:",total)
print("count:",count)


#4
n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()

for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()



