import numpy as np
import time
import sys

thinking_animatiion(duration = 5):
    print("I'm thinking",end ="")

    for i in range(duration * 2):
        time.sleep(0.5)
        print(".",end ="")
        sys.stdout.flush()
    print("\n")

rng = np.random.default_rng()


name = input("What's your name? ")
first_name,last_name = name.split(" ")

while(True):
    print(f"Welcome to the Game {first_name} 🙏")
    print()
    user_choice_number0 = int(input("Select your choice: 1.Scissor 2.Papper 3.Rock \n"))
    coumputer_choice_number = rng.integers(0,3)
    user_choice_number = user_choice_number0 - 1
    if(coumputer_choice_number == 0):
        comupter_choice = "✂️"
    elif(coumputer_choice_number == 1):
        comupter_choice = "📃"
    else:
        comupter_choice = "🪨"


    if(user_choice_number == 0):
        user_choice = "✂️"
    elif(user_choice_number == 1):
        user_choice = "📃"
    elif(user_choice_number == 2):
        user_choice = "🪨"
    else:
        print("Invalid selection")
        continue
    print(f"Your Choice is {user_choice}")
    
    print()

    thinking_animatiion(4)

    print(f"Computer Choice is {comupter_choice}")
  
    print()


    if((user_choice_number == 0 and coumputer_choice_number == 1) or 
       (user_choice_number == 1 and coumputer_choice_number == 2) or
       (user_choice_number == 1 and coumputer_choice_number == 0)):
        print("You are win 🏆")
        break
    elif((user_choice_number == 0 and coumputer_choice_number == 0) or 
       (user_choice_number == 1 and coumputer_choice_number == 1) or
       (user_choice_number == 2 and coumputer_choice_number == 2)):
        print("Match is tie 🙌")
    else:
        print("You are fail 😔")
        




