import random

b = [" ", " ", " ",
     " ", " ", " ",
     " ", " ", " "]


def show_board():
    return f"{b[0]}|{b[1]}|{b[2]}\n{b[3]}|{b[4]}|{b[5]}\n{b[6]}|{b[7]}|{b[8]}"


def win_terms(v):
    if b[0] == v and b[1] == v and b[2] == v:
        return True
    elif b[3] == v and b[4] == v and b[5] == v:
        return True
    elif b[6] == v and b[7] == v and b[8] == v:
        return True
    elif b[0] == v and b[4] == v and b[8] == v:
        return True
    elif b[2] == v and b[4] == v and b[6] == v:
        return True
    elif b[0] == v and b[3] == v and b[6] == v:
        return True
    elif b[1] == v and b[4] == v and b[7] == v:
        return True
    elif b[2] == v and b[5] == v and b[8] == v:
        return True

    return False


player = "x"
npc = "o"
win = False

print(show_board())

while not win:

    h_choice = int(input("Enter a position (1-9): "))

    if h_choice not in range(1, 10):
        print("Invalid position!")
        continue

    if b[h_choice - 1] != " ":
        print("That square is already occupied!")
        continue

    b[h_choice - 1] = player

    if win_terms(player):
        print(show_board())
        print("Player won!")
        win = True
        break

    while True:
        npc_c = random.randint(0, 8)

        if b[npc_c] == " ":
            b[npc_c] = npc
            break

    print(show_board())

    if win_terms(npc):
        print("NPC won!")
        win = True