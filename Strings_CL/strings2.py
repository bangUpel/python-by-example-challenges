#first challenge
first_name = input('enter ur first name : ')
surname = input('enter ur  surname : ')
print(f'ur first name has {len(first_name)} characters and ur surname has {len(surname)} in it')
full_name = first_name + ' ' + surname
print(f'it means, ur full name({full_name}) will have characters {len(full_name)} in it')

#second challenge
subject = input('enter ur favorite subject in school : ')
for char in subject:
    print(char,end='-')

#third challenge
poem = 'rose is red, violet is blue, you\'re perfect, so i love you'
print(poem)
start = int(input('enter the start num : '))
end = int(input('enter the end num : '))
print(poem[start:end])

#fourth challenge
upper_word = input('please enter a word in uppercase : ')
while upper_word.islower() or upper_word == '':
    upper_word = input('PLEASE ENTER A WORD IN UPPERCASE : ')
print('ok thank you')

#fifth challenge
post = input('enter ur postcode : ')
start = post[0:2]
print(start.upper())

#sixth challenge
name = input('please enter ur name : ')
count = 0
for i in name:
    if i in ['a','i','u','e','o']:
        count += 1
print(f'there is {count} vowel in ur name')

#seventh challenge
password = input('enter a new password : ')
validate_password = input('enter ur password again : ')
if password == validate_password:
    print('thank you')
elif password.lower() == validate_password.lower():
    print('u should enter it in the same case')
else:
    print('incorrect')
    
#eight challenge
word = input('enter a word : ')
length = len(word)
num = 1
for char in word:
    position = length - num
    print(position)
    letter = word[position]
    print(letter)
    num = num + 1