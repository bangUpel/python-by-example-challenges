#first challenge 
name = str(input('masukkan nama anda : '))
print('nama anda mempunyai panjang ', len(name), 'karakter')

#second challenge
first_name = str(input('Masukkan first name anda : '))
surname = str(input('Masukkan surname anda : '))
name = first_name + ' ' + surname
print('nama lengkap anda adalah', name,'dan nama anda mempunyai panjang', len(name), 'karakter')

#third challenge
first_name = str(input('Masukkan first name anda (DALAM HURUF KECIL) : '))
surname = str(input('Masukkan surname anda (DALAM HURUF KECIL) : '))
name = first_name + ' ' + surname
print(f'nama anda adalah {name.title()}')

#fourth challenge
word = str(input('GIVE ME A RANDOM WORD!!! : '))
print(f'ur word has {len(word)} character in it, I WANT TO SLICE IT!!!') 
len1 = int(input('GIMME THE START SLICE : '))
len2 = int(input('GIMME THE END SLICE : '))
print(f'the slice result is {word[len1:len2]}')

#fifth challenge 
word = str(input('GIMME A RANDOM WORD AGAIN : '))
print(f'The capitalize version of ur word is {word.upper()}')

#sixth challenge
first_name = str(input('enter ur first name : '))
if len(first_name) < 5:
    surname = str(input('enter ur surname : '))
    name = first_name + surname
    print(f'ur name is {name.upper()}')
else:
    print(f'ur name is {first_name.lower()}')

#seventh challenge
word = str(input('enter a random word : '))
word = word + word[0]
word_char = len(word)
word = word[1:word_char]
word = word + 'ay'
print(word)

