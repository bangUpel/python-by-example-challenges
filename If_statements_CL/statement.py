#first challenge 
fnum = int(input('masukkan angka pertama :'))
lnum = int(input('masukkan angka kedua :'))
if fnum > lnum:
    print(fnum,lnum)
else:
    print(lnum,fnum)

#second challenge
num = int(input('masukkan angka yg lebih kecil dari 20 : '))
if num < 20:
    print("makasih!")
else:
    print("angkanya kebesaran")

#third challenge
num = int(input('masukkan angka diantara 10 sampai 20 : '))
if num >= 10 and num <= 20:
    print("makasih!")
else:
    print('jawaban salah')

#fourth challenge
color = str(input('masukkan warna yg kau sukai : '))
color = str.lower(color)
if color == 'merah':
    print("aku juga suka warna merah!")
else:
    print(f'aku tidak suka warna {color}, merah lebih bagus')

#fifth challenge
weather = str(input('Apakah hari sedang hujan? [y/n] : '))
weather = str.lower(weather)
if weather == "y":
    windy = str(input('apakah anginnya kencang? [y/n] : '))
    windy = str.lower(windy)
    if windy == "y":
        print('kurasa payung tidak akan bisa bertahan')
    elif windy == "n":
        print('membawa payung kurasa ide bagus')
    else:
        print('jawaban invalid')
elif weather == "n":
    print('selamat menikmati harimu!')
else:
    print('jawaban invalid.')

#sixth challenge
age = int(input('masukkan umurmu (dalam tahun): '))
if age >= 18:
    print('kamu boleh voting')
elif age == 17:
    print('kamu bisa belajar mengemudi')
elif age == 16:
    print('kamu bisa membeli tiket lotre')
elif age > 16:
    print('kamu bisa melakukan trick-or-treat!')
else:
    print('jawaban invalid')

#seventh challenge
num = int(input('masukkan angka dari 10-20'))
if num >= 10 and num <= 20:
    print('correct')
elif num < 10:
    print('angka terlalu kecil')
elif num > 20:
    print('angka terlalu besar')
else:
    print('jawaban invalid')

#eight challenge
num = int(input('choose number between 1, 2, 3'))
if num == 1:
    print('thank you')
elif num == 2:
    print('well done')
elif num == 3:
    print('correct')
else:
    print('jawaban invalid')