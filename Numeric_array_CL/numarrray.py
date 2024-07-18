from array import *
import random

#first challenge
num = array ('i', [])
for x in range (0,5):
    append = int(input('enter a number : '))
    num.append(append)
num.reverse()
print(num)

#second challenge
num = array ('i', [])
for x in range(0,5):
    random_number = random.randint(0,100)
    num.append(random_number)
    print(num[x])

#third challenge
num = array ('i', [])
while(len(num) != 5):
    ask_num = int(input('enter a number (10-20 ): '))
    if ask_num >= 10 and ask_num <=20:
        num.append(ask_num)
    else:
        print('try again')
print('out of range')
for x in num:
    print(x)

#fourth challenge
num = array ('i', [2,4,2,3,4])
print(num)
show_rep = int(input("pick a number in the array above :"))
print(f'there is {num.count(show_rep)} number of {show_rep} in the array')

#fifth challenge
arr_random = array('i', [])
num = array ('i', [])
for x in range (0,5):
    arr_random.append(random.randint(1,10))
for x in range (0,3):
    num_add = int(input('enter a number : '))
    num.append(num_add)
arr_random.extend(num)
new_array = sorted(arr_random)
for x in new_array:
    print(x)

#sixth challenge
num = []
for x in range (0,5):
    add_num = int(input("enter a number : "))
    num.append(add_num)
print(f'ur array is : \n{num}')
pick = int(input("please pick a number from ur array :"))
if pick in num:
    num.remove(pick)
    new_arr = []
    new_arr.extend(num)
    print(new_arr) #dont ask me, it will be easier to write *print(num)* but the task told me to do like this
else:
    print(f"there is no {pick} in ur array")
    
#seventh challenge
arr = [65,34,86,23,75]
tryagain = True
while tryagain == True:
    print(arr)
    pick = int(input("select a number from array above :"))
    if pick not in arr:
        print(f"there is no {pick} in the array")
    else:
        print(f'the index of {pick} is {arr.index(pick)}')
        tryagain = False

#eight challenge
arr = [25.02, 10.02, 19.03, 10.4, 69.8]
new_arr = []
tryagain = True
while tryagain == True:
    print(arr)
    num_divide = int(input("enter a number from 2-5 to divide :"))
    if num_divide >= 2 and num_divide <= 5:
        for x in arr:
            divided = x / num_divide
            new_arr.append(divided)
        print(new_arr)
        tryagain = False
    else:
        print('please enter a valid number') 