import random

#first challenge
file = open("Text[W&R]_CL/numbers.txt", "a")

for x in range (0,5):
    if x == 4:
        file.write(f'{random.randint(1,10)}\n')
    else:
        file.write(f'{random.randint(1,10)},')
file.close()

#second challenge
file = open("Text[W&R]_CL/names.txt", "w")
char_id = ['a', 'f', 'u', 'd', 'n']
full_name = []
number_of_names = 5
name_length = 4
for _ in range(number_of_names):
    name = []
    for _ in range(name_length):
        char = char_id[random.randint(0, len(char_id) - 1)]
        name.append(char)
    result = ''.join(name)
    full_name.append(result)
for x in range(5):
    file.write(full_name[x] + '\n')
file.close()

#third challenge
file = open("Text[W&R]_CL/names.txt", "r")
print(file.read())

#fourth challenge
file = open("Text[W&R]_CL/names.txt", "r")
print(file.read())
file = open("Text[W&R]_CL/names.txt", "a")
new_name = input("enter a new name to add : ")
file.write(new_name)
file = open("Text[W&R]_CL/names.txt", "r")
print(file.read())
file.close()

#fourth challenge
repeat = True
while repeat:
    print('''
==============================
 1. create a new file
 2. display the file
 3. add a new subject to the file
 4. exit
==============================
      ''')
    try:
        file_op = int(input("make a selection 1, 2, 3, or 4 :"))
        if file_op == 1:
            file = open("Text[W&R]_CL/subject.txt", "w")
            subject = input("enter a new school subject : ")
            file.write(subject)
            file.close()
        elif file_op == 2:
            file = open("Text[W&R]_CL/subject.txt", "r")
            print(file.read())
        elif file_op == 3:
            file = open("Text[W&R]_CL/subject.txt", "a")
            add_subject = input("add a new subject : ")
            file.write('\n' + add_subject)
            file.close()
            print("new subject added.")
        elif file_op == 4:
            repeat = False
        else:
            print("out of range.")
    except ValueError:
        print("invalid value")
    except Exception as e:
        print("error happened :", e)
        continue

#fifth challenge
file = open("Text[W&R]_CL/names.txt", "r")
print(file.read())
file.close()
file = open("Text[W&R]_CL/names.txt", "r")
move = input("enter a name to move : ")
move_name = move + '\n'
for x in file:
    if x != move_name:
        file = open("Text[W&R]_CL/names2.txt", "a")
        file.write(x)
        file.close()
file.close()
