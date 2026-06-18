import random
#get a random number!
computer_number = random.randint(1 , 10)
#place holder!
guess = 0 
#function for WIN!
def win(computer_number, guess):
    return computer_number == guess
    
#a function that gets your number!
def get_input():
    return int(input("write your guess"))

#check either you guessed correctly or not
def answer(computer_number, guess):
    if computer_number > guess:
        result = "my number is larger" 
    elif computer_number < guess:
        result  = "my number is smaller"
    else:
        result = f"correct! computer number is {computer_number}"

#program will not stop until you win
while(not win(computer_number , guess)):
    guess = get_input()
    print(answer(computer_number, guess))
