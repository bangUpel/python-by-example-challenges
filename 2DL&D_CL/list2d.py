#first challenge
matrix = [
    [2,5,8],
    [3,7,4],
    [1,6,9],
    [4,2,0]
]
print(matrix)

#second challenge
matrix = [
    [2,5,8],
    [3,7,4],
    [1,6,9],
    [4,2,0]
]
show_matrix = int(input("select a row to display 1-4 :"))
show_matrix -= 1
print(matrix[show_matrix])

#third challenge
matrix = [
    [2,5,8],
    [3,7,4],
    [1,6,9],
    [4,2,0]
]
show_matrix = int(input("select a row to display 1-4 :"))
show_matrix -= 1
print(matrix[show_matrix])
add_matrix = int(input("enter a new number to add in ur matrix : "))
matrix[show_matrix].append(add_matrix)
print(matrix[show_matrix])

#fourth challenge
matrix = [
    [2,5,8],
    [3,7,4],
    [1,6,9],
    [4,2,0]
]
show_matrix = int(input("select a row to display 1-4 :"))
show_matrix -= 1
print(matrix[show_matrix])
col_show = int(input("which column u want to display 1-3 : "))
col_show -= 1
print(matrix[show_matrix][col_show])
ask_change = input("change value : [y/n]")
if ask_change == "y":
    new_col = int(input("new value : "))
    matrix[show_matrix][col_show] = new_col
    print(matrix[show_matrix])

#fifth challenge
cdn = {
    "John" : {"N" : 3056, "S" : 8463, "E" : 2353, "W" : 5378},
    "Tom" : {"N" : 5367, "S" : 6442, "E" : 5327, "W" : 7453},
    "Anna" : {"N" : 7353, "S" : 7624, "E" : 7532, "W" : 8664},
    "Vionetta" : {"N" : 2456, "S" : 1463, "E" : 3254, "W" : 9753}
}
for x in cdn:
    print(x,cdn[x])
sales = int(input("enter the sales index (1-4): "))
names = {
    1: "John",
    2: "Tom",
    3: "Anna",
    4: "Vionetta"
}
region = input("enter a region : (N, S, E, W) ")
names_acc = names.get(sales)
print(cdn[names_acc][region])
new_data = int(input("enter new data : "))
cdn[names_acc][region] = new_data
print(cdn[names_acc])

#sixth challenge
list = {}
for x in range(1,5):
    name = input("enter a name : ")
    name = name.upper()
    age = int(input("enter the person's age : "))
    shoe = int(input("enter a shoe size : "))
    list[name] = {"age" : age, "shoe size" : shoe}
for x in list:
    print(x,list[x])
pick = input("enter a name : ")
pick = pick.upper()
print(list[pick])


#seventh shallenge
list = {}
for x in range(1,3):
    name = input("enter a name : ")
    name = name.upper()
    age = int(input("enter the person's age : "))
    shoe = int(input("enter a shoe size : "))
    list[name] = {"age" : age, "shoe size" : shoe}
for x in list:
    print(x,list[x]["age"])

#eight challenge
list = {}
for x in range(1,5):
    name = input("enter a name : ")
    name = name.upper()
    age = int(input("enter the person's age : "))
    shoe = int(input("enter a shoe size : "))
    list[name] = {"age" : age, "shoe size" : shoe}
for x in list:
    print(x,list[x])
pick = input("enter a name : ")
pick = pick.upper()
del list[pick]
for x in list:
    print(x,list[x])