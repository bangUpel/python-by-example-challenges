import random

#first challenge
num = random.randint(0,100)
print(num)

#second challenge
fruit = ['apple','banana', 'melon', 'watermelon', 'grape']
print(random.choice(fruit))

#third challenge
condition = random.choice(['h', 't'])
choose = input('guess, head or tail [h/t]: ')
choose = choose.lower()
if choose == condition:
    print('You win!')
else:
    print('You lose!')

#fourth challenge
cnum = random.choice([1,2,3,4,5])
for i in range (1,3):
    guess = int(input('guess the correct number! (1-5) : '))
    if guess > cnum:
        print('too big')
    elif guess < cnum:
        print('too low')
    else:
        print('Well done!')
        exit()
print('You lose!')

#fifth challenge
num = random.randint(0,10)
choose = int(input('guess the correct number! (0-10) : '))
while num != choose:
    print('U are wrong, try again!')
    choose = int(input('guess the correct number! (0-10) : '))
print('U guess it correctly!')

#sixth challenge
num = random.randint(0,10)
choose = ''
while num != choose:
    choose = int(input('guess the correct number! (0-10) : '))
    if choose > num:
        print('too high!')
    elif choose < num:
        print('too low!')
    else:
        print('U guess it correctly!')

#seventh challenge
score = 0
for loop in range (1,6):
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    num = num1 + num2
    answer = int(input(f'{num1} + {num2} is equal to : '))
    if answer == num:
        print('correct.')
        score += 20
    else:
        print('incorrect')
        continue
print(f'ur score is {score}!')

#eight challenge
color = random.choice(['white', 'blue', 'red', 'black', 'yellow'])
print('there is five color : White, blue, red, black, yellow\nchoose the color that I like!')
guess = ''
while guess != color:
    guess = input('what is my favorite color : ')
    guess = guess.lower()
    if color == guess:
        continue
    elif color == 'blue':
        print('I think u are feeling BLUE rn')
    elif color == 'white':
        print('Do u know that ur bone is WHITE?')
    elif color == 'red':
        print('Ur blood is RED, isn\'t it?')
    elif color == 'black':
        print('N**** got BLACK skin, dont u know?')
    elif color == 'yellow':
        print('ur skin look so YELLOW, are u sick? ')
print('U guess it correctly! :3')