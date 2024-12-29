import random

print("welcome to rock-paper-scissors!")
print("choose Rock,Paper and Scissor")

user_choice = input("Enter your choice(rock,paper and scissor): ").lower()

computer_choice = random.choice(["rock","paper", "scissor"])

print(f"Your's choice : {user_choice}")
print(f"computer's choice: {computer_choice}")

if user_choice == computer_choice:
    print("It,s a Tie !")

elif(user_choice == "paper" and computer_choice == "rock") or \
    (user_choice == "rock" and computer_choice == "scissor") or \
    (user_choice == "scissor" and computer_choice == "paper"):
    print("You Win !")

else:
    print("You Lose !")    



