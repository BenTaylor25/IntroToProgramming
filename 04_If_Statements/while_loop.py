
num = 4  # random number
guess = 0

while num != guess:
    guess = int(input("Guess my number: "))
    
    if guess > num:
        print("too high")
    elif guess < num:
        print("too low")

print("correct")
