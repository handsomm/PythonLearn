import random


def game(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


randNo = random.randint(1, 3)

if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Player's Turn: Snake(s), Water(w) or Gun(g)?\n")

a = game(comp, you)

print(f"Computer choose: {comp}")
print(f"You choose: {you}")

if a == None:
    print("The game is Tie!")
elif a:
    print("You win !!!")
else:
    print("You lose ???")
