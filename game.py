import random
name= input("What is your name?")
print("welcome " + name)
choices= ("rock", "paper", "scissors")
computer_choice = random.choice(choices) 
print("type rock, paper, scissors to play or 'quit' to exit.\n")
player_score=  0
computer_score= 0
while True:
    player_choice = input("Your choice").lower().strip()
    if player_choice== "quit":
        print("\n thank you for playing!")
        break
    if player_choice not in choices:
        print("\ninvalid choice. please type rock, paper, scissors")
        print(f"Computer chose: {computer_choice}")
    if player_choice == computer_choice:
            print("It's a tie!")
    elif(
            (player_choice=="rock" and computer_choice=="scissors")or
            (player_choice=="paper" and computer_choice=="rock")or
            (player_choice=="scissors" and computer_choice=="paper")
        ):
            print("Congrats you win this round!")
            player_score +=1
    else:
            print("Computer wins this round!")
            computer_score +=1
            print(f"Score -> You: {player_score} | Computer: {computer_score}\n")





    
