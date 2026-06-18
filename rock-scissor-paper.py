import random
game_play = {"r":"s" , "s":"p" , "p":"r"}
choice = ["r", "s" , "p"]
def gameplay():
    cu_choice = random.choice(choice)
    human = input("enter your choice(r/s/p)").lower()
    if human not in game_play:
        raise ValueError(f"{human} is not defined as a game action")
    
    if cu_choice == human :
        return "draw " f"computer choice was {cu_choice}"
    elif game_play[human] == cu_choice:
        return "you won " f"computer choice was {cu_choice}"
    else:
        return "you lost " f"computer choice was {cu_choice}"



