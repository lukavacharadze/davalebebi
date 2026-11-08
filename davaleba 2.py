#1
word="programming"
print(word[0])
print(word[-1])
print(word[-3])
print(word[:4])
print(word[-4:])
print(word[0:11:2])
print(word[::-1])

#2
mail=input("enter your mail:")
index=mail.find('@')
saxeli = mail[:index]
print(saxeli)

domain = mail[index+1:]
print(domain)

index2=mail.find('.')
domain2 = mail[index+1:index2]
print(domain2)

#3
number=input("enter your number:")
print(number.replace(" ","").replace("-",""))

#4
headline=input("enter your headline:")
print(headline.lower().replace(' ','-').strip())

#5
name=input("enter your name:")
age=input("enter your age:")
city=input("enter your city:")
language=input("enter your favorite language:")

print(f'{name.title()})')
print(f'{age})')
print(f'{city.title()}')
print(f'{language.upper()}')