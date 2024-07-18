#INFORMATION ABOUT STRING

#len(string) -> untuk mencari berapa 'panjang' string
word = "Aufa Robbani"
print (len(word)) #the output will be : 12

#.upper() -> untuk mengkapital kan setiap huruf dalam string
print(word.upper()) # the output will be : AUFA ROBBANI

#.lower() -> untuk mengecilkan setiap huruf dalam string
print(word.lower()) # the output will be : aufa robbani

#.capitalize() -> untuk membuat huruf pertama dalam string menjadi kapital
print(word.capitalize()) #the output will be : Aufa robbani

#.title() -> untuk membuat string seakan2 menjadi judul cerita, dimana tiap kata pasti dikapital kan
title = "anjay slebew"
print(title.title()) #the output will be : Anjay Slebew

#.strip() -> Removes extra characters (in this case spaces) from the start and end of a string.
kata = " aku adalah superman "
print(kata.strip(" "))

#string[num:num] -> Each letter is assigned an index number to identify its position in the phrase, including the space. Python starts counting from 0, not 1
word = "Hello world!"
print(len(word), word[7:10]) #word[7:10] output will be : 'orl'