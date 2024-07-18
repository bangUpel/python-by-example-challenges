#first challenge
countries = ('indonesia', 'malaysia', 'japan', 'korea', 'turkey')
print(countries)
answer = input('please enter a country name from the tuple : ')
if answer in countries:
    print(f'the position of country u entered is {countries.index(answer)+1}')

#second challenge
countries = ('indonesia', 'malaysia', 'japan', 'korea', 'turkey')
print(countries)
answer = int(input('please enter a country number (1-5) : '))
if answer <= 5 and answer > 0:
    print(f'the country with position of {answer} is  {countries[answer-1]}')

#third challenge
sport = ['football', 'volly']
fav = input('enter ur favorite sport? : ')
sport.append(fav)
sport.sort()
print(sport)

#fourth challenge
subject = ['math', 'physics', 'english', 'biology', 'aswaja']
print(subject)
delete = input('enter 1 subject name u do not like : ')
subject.remove(delete)
print(subject)

#fifth challenge
food_dict = {}
for i in range (1,5):
    food_dict[i] = (input('enter ur favorite food : '))
print(f'so, ur favorite foods is :\n{food_dict}')
answer = int(input('which one u wanna take with u : '))
del food_dict[answer]
print(sorted(food_dict.values()))

#sixth challenge
colours = ['merah', 'kuning', 'hijau', 'ungu', 'hitam', 'putih', 'biru', 'coklat', 'abu-abu', 'pink']
start_num = int(input('enter a start number (0-4): '))
end_num = int(input('enter a end number (5-9): '))
print(colours[start_num:end_num])

#seventh challenge
numbers = [123, 321, 697, 999]
for i in range(0,len(numbers)):
    print(numbers[i])
matches = int(input('enter a number : '))
if matches in numbers:
    print(f'{matches} position is equal to {numbers.index(matches)+1}')
else:
    print('that is not in the list')

#eight challenge
person = []
for i in range (0,3):
    invite = input(f'enter the name of person {i + 1} : ')
    person.append(invite)
print(f'{person} have been invited!')
more_person = input('do u want to invite another person? [y/n] : ')
more_person.lower()
while more_person == 'y':
    if more_person == 'y':
        invite = input(f'enter the person name : ')
        person.append(invite)
    elif more_person == 'n':
        print(f'u have been invited {len(person)} person in to the party! ')
        exit()

#ninth challenge
person = []
for i in range (0,3):
    invite = input(f'enter the name of person {i + 1} : ')
    person.append(invite)
print(f'{person} have been invited!')
more_person = input('do u want to invite another person? [y/n] : ')
more_person = more_person.lower()
if more_person == 'y':
    while more_person == 'y':
        invite = input(f'enter the person name : ')
        person.append(invite)
        more_person = input('do u want to invite another person? [y/n] : ')
        more_person = more_person.lower()
    if more_person == 'n':
        print(f'u have been invited {len(person)} person in to the party! ')

#tenth challenge
person = []
for i in range (0,3):
    invite = input(f'enter the name of person {i + 1} : ')
    person.append(invite)
print(f'{person} have been invited!')
more_person = input('do u want to invite another person? [y/n] : ')
more_person = more_person.lower()
if more_person == 'y':
    while more_person == 'y':
        invite = input('enter the person name : ')
        person.append(invite)
        more_person = input('do u want to invite another person? [y/n] : ')
        more_person = more_person.lower()
        if more_person == 'n':
            print(f'{person} have been invited! ')
            name_person = input('enter a name of a person : ')
            if name_person in person:
                print(f'{name_person} has position of {person.index(name_person)+1}')
            else:
                print('invalid input')
            take_person = input(f'do u want {name_person} to come in to ur party? [y/n] : ')
            take_person = take_person.lower()
            if take_person == 'y':
                print(f'{name_person} is invited to ur party.')
            elif take_person == 'n':
                person.remove(name_person)
                print(f'{name_person} has been kicked, {person} have been invited to the party.')
            else:
                print('invalid input')
        else:
            print('answer is invalid')
elif more_person == 'n':
    print('3 person has invited to ur party')
else:
    print('answer is invalid')

#eleventh challenge
tv = ['antv', 'globalTV', 'RCTI', 'JTV']
for i in tv:
    print(i)
tv_put = input('enter a new tv channel : ')
tv_new = int(input('what lines u want to put the new channel : '))
tv.insert(tv_new-1,tv_put)
for i in tv:
    print(i)

#twelveth challenge
num = []
for i in range (0,3):
    num_add = int(input(f'put the number in position {i+1} :'))
    num.append(num_add)
print(num)
num_save = input(f'do u want to remove {num[2]} from the list? [y/n] : ')
num_save = num_save.lower()
if num_save == 'y':
    num.remove(num[2])
    print(num)
else:
    print(num)