
with open('08_Files/test2.txt', 'w') as file:
    file.write("hello")

with open('08_Files/test2.txt', 'a') as file:
    file.write(" goodbye")
