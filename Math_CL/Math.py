import math
#first challenge
num = float(input('enter a decimal number : '))
decimal = num*2
print(decimal)

#second challenge
num = float(input('enter a decimal number : '))
decimal = num*2
print(round(decimal,2))

#third challenge
num = int(input('enter a number over 500 : '))
if num > 500:
    print(round(math.sqrt(num),2))
else:
    print('dongo')

#fourth challenge
print(round(math.pi,5))

#fifth challenge
num = int(input('enter the radius of the circle : '))
luas = math.pi * num**2
print(f'luas lingkaran adalah {luas}')

#sixth challenge
depth = int(input('enter the cylinder depth : '))
radius = int(input('enter the circle radius : '))
area = math.pi* radius**2
print(f'the cylinder volume is equal to {round(area,3)}')

#seventh challenge
num1 = int(input('enter the first number to divide :'))
num2 = int(input('now, enter the second number : '))
bagi = num1 // num2
sisa = num1 // num2
print(f'{num1} divided by {num2} is {bagi} with {sisa} remaining')

#eight challenge
print('1)Square\n2)Triangle')
choose = int(input('Enter a number : '))
if choose == 1:
    sisi = int(input('enter the side length : '))
    area = sisi**2
    print(f'square are with {sisi} side length is {area}')
elif choose == 2:
    alas = int(input('enter the base : '))
    tinggi = int(input('enter the height : '))
    area = 0.5 * alas * tinggi
    print(f'triangle are is equal to {area}')
else:
    print('input is invalid')