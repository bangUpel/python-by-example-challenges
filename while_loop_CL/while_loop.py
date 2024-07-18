#first challenge
total = 0
num = int(input('masukkan angka : '))
total = num
while total < 50:
    num = int(input('masukkan angka untuk dijumlahkan : '))
    total += num
print(total)


#second challenge
num = int(input('enter a number : '))
while num <= 5:
    num = int(input('enter a number : '))
print(f'the last number u put is {num}')

#third challenge
num1 = int(input('enter a number : '))
total = num1
again = "y"
while again == "y":
    num2 = int(input('enter a number to add : '))
    total +=num2
    again = input('want to add more number? [y/n]')
    again = again.lower()
print(total)

#fourth challenge
more = 'y'
count = 0
while more == 'y':
    name = input('enter the name of person u invited : ')
    print(f'{name} has been invited!')
    count += 1
    more = input('do u want to invite more people? [y/n] : ')
print(f'there is {count} people u have invited!')

#sixth challenge
correct = 50
answer = 0
attempt = 0
while answer != correct:
    answer = int(input('guess the correct number! : '))
    if answer > correct:
        print('Too high!')
        attempt += 1
    elif answer == correct:
        attempt += 1
    else:
        print('too low!')
        attempt += 1
print(f'u guess it correctly in {attempt} attempts!')

#seventh challengethe
guess = 0
while guess < 10 or guess > 20:
    guess = int(input('guess one of the number in area that is correct! : '))
    if guess > 20:
        print('too high')
    elif guess < 10:
        print('too low')
print('thank you!')

#eight challenge
bottle = 10
guess = 0
while guess != bottle:
    print(f'''There are {bottle} green bottles hanging on the wall,
{bottle} green bottles hanging on the wall, 
and if 1 green bottle should accidentally fall.''')
    bottle -= 1
    guess = int(input('how many bottles are left? : '))
    if guess == bottle:
        print(f'There will be {bottle} green bottles hanging on the wall.')
    elif bottle == 0:
        print('there are no more bottles...')
        exit()
    else:
        print('no, try again')