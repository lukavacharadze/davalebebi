#1
shopping=["milk","bread","eggs"]
shopping.append('cheese')
print(shopping)
shopping.insert(0,"apples")
print(shopping)
shopping[-1]="butter"
print(shopping)
shopping.extend(['coffee','orange'])
print(shopping)
shopping.pop(1)
print(shopping)
delete=shopping.pop(1)
print(shopping)
print(delete)

#2
scores = [85, 92, 78, 92, 65, 88, 92]
copiedscores=scores.copy()
print("count of 92:",copiedscores.count(92))
print("index of 78:",copiedscores.index(78))
copiedscores.sort()
print('ascending:',copiedscores)
copiedscores.sort(reverse=True)
print('descending:',copiedscores)
print("highest",copiedscores[0])
print("lowest",copiedscores[-1])
print(scores)

#3
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("rows:",len(matrix))
print('last row:',matrix[-1])
print("number 6:",matrix[1][2])
print("negative 6:", matrix[-2][-1])
print("negative 7:",matrix[-1][-3])
matrix[1][1]=50
print("new matrix:",matrix)


#4
numbers =[]

while True:
    user_input=input("Enter a number:")
    if user_input=="stop":
        break

    numbers.append(int(user_input))
print("numbers:",numbers)
print("count:",len(numbers))
if len(numbers)>0:
    print("first number:",numbers[0],"last number:",numbers[-1])
descending=numbers.copy()
descending.sort(reverse=True)
print("descending:",descending)











