
def get_num():
    num = input("Enter an integer: ")
    return int(num)

def add(num1, num2):
    return num1 + num2

def program():
    num1 = get_num()
    num2 = get_num()
    print( add(num1, num2) )


program()
