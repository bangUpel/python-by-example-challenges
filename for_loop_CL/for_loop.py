#first challenge

name = str(input('enter ur name here : '))
for i in range(0,3):
    print(name)

#second challenge
name = str(input('enter ur name here : '))
loop = int(input('enter the loop value here : '))
for i in range(0,loop):
    print(name)

#third challenge
name = str(input('enter ur name here : '))
for i in name:
    print(i)

#fourth challenge
name = str(input('enter ur name here : '))
loop = int(input('enter the loop value here : '))
for i in range(0,loop):
    for i in name:
        print(i)


#fifth challenge
num = int(input('enter a number between 1 and 12 : '))
for i in range(1,13):
    answer = i * num
    print(f'{i}*{num} is equal to {answer}')

#sixth challenge 
num = int(input('enter a number below 50 : '))
for i in range(50,num,-1):
    print(i)
print(num)

#seventh challenge
name = str(input('enter ur name here : '))
loop = int(input('enter the loop value here (must be below 10) : '))
if loop < 10 :
    for i in range(0,loop):
        print(name)
else:
    print('Too high\n' * 3)

#eight challenge
total = 0
for i in range (1,6):
    num1 = int(input(f'put the number {i} here : '))
    validate = str(input('do u want to add it in total? [y/n]'))
    validate = validate.lower()
    if validate == "y":
        total += num1
    else:
        continue
print('the total is equal to ',total)

#ninth challenge
direction = str(input('what direction u prefer (up or down) : '))
direction = direction.lower()
if direction == 'up':
    num = int(input('enter the max number : '))
    for i in range(1,num):
        print(i)
    print(num)
elif direction == 'down':
    num = int(input('enter a number below 20 : '))
    for i in range(20,num,-1):
        print(i)
    print(num)
else:
    print('I dont understand')

#tenth challenge
people = int(input('how many person u want to invite : '))
if people < 10:
    for i in range(0,people):
        name = str(input('enter the person name : '))
        print(f'{name} has been invited to the party')
elif people >= 10:
    print('too much')
else:
    print('huh?')