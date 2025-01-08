import random as r

computerGuess = r.randint(1, 10)
max_attempt = 5

for i in range(max_attempt):
    print("guess the number\n")
    userNumber = int(input())
    if userNumber == computerGuess:
        print(f"You Won, your guess {userNumber} and {computerGuess} is same.")
        break
    else:
        if userNumber > computerGuess:
            print("Hint: Your guess is greater then the computer guess.")
        else:
            print("Hint: Your guess is smaller then the computer guess.")
            print(f"{max_attempt - i} attempt left")