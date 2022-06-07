health = 10

gameLoop = True
while gameLoop:
    action = input("-->")
    if action == "hp":
        print(health)
    elif action == "hit":
        health -= 1
    elif action == "heal":
        health += 3
    elif action == "exit":
        gameLoop = False
