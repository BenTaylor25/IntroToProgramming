def read_file(filename):
    with open(filename) as file:
        return file.read()

def readline_file(filename):
    with open(filename) as file:
        return file.readline()

def readlines_file(filename):
    with open(filename) as file:
        return file.readlines()

def readsplitlines_file(filename):
    with open(filename) as file:
        return file.read().splitlines()
   

print(read_file("08_Files/test.txt"))
print('~')
print(readline_file("08_Files/test.txt"))
print('~')
print(readlines_file("08_Files/test.txt"))
print('~')
print(readsplitlines_file("08_Files/test.txt"))
