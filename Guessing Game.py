number = 4
chance = 0
limit = 3
while chance<limit:
    guess = int(input('Guess: '))
    chance=chance+1
    if guess == number:
        print("You win!")
        break
else:
    print("Sorry, you failed!")