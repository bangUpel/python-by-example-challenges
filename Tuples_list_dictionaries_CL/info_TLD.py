#this code is for information about tuples, list and dictionary only
import random

#TUPLES
fruit_tuple = ('apple', 'banana', 'melon', 'grape')

print(fruit_tuple)
print(fruit_tuple * 2) #u can only use * operator for tuple
print(fruit_tuple.index('banana')) # show u the index of the item
print(fruit_tuple[1]) #output will be index 1 of tuple, which is banana

#LIST
name_list = ['aufa', 'john', 'burhan', 'yanto']

print(name_list)
print(name_list * 2)
print(name_list.index('aufa'))
del name_list[random.randint(0,3)] #delete random item for list
print(name_list)
name_list.append(input('add a name : ')) #put a new item in list
print(name_list)
print('sort but dont change : ',sorted(name_list)) #sort list but dont really change it
print(f'real version {name_list}')
name_list.sort() #change the list in to sorted version (in alphabetical order)
print(f'the alphabetical sort of name list is {name_list}')
name_list[0] = 'yellow' #change the index 0 of list in to 'yellow'
print(name_list)
print(len(name_list))

#DICTIONARY
colours = {
    1:'red',
    2:'blue',
    3:'green',
    4:'purple',
    5:'yellow'
    }
print(colours[random.randint(1,5)])
colours[3] = 'black' #change index 3 of dict in to 'black'
print(colours)

#NUMERIC LIST
x = [20,30,4,7,69,101]
print(x)
print(len(x)) #output will be the length of the list
print(x[1:3]) #this will print list, within start from index 1 and will over before the index 3, so output = [30,4]
for i in x:
    print(i) #this will print items in list on separate lines
num = int(input('enter a number in numberic list : '))
if num in x: #in -> syntax for checking, do the num is in the list, while yes -> true -> execute program
    print('OK Thank you')
else:
    print(f'there is no {num} in numberic list')
x.insert(0,8) #this will add number 8 to index 0 of list, and the other items will be pushed, so the index of 20(item) will added by 1, the others also
print(x)
x.append(101) #this will add a new item in the list
print(x)
x.remove(101) #this will remove item = 101 from list, if there is more than 1, it will delete the first item(which is 101) from list only
print(x)