import random

#number of games
games_number=1
max_games=5

#number of chances in a game
chances=5

#difficulty level
difficulty = 0

score= []

#input for difficulty level
while difficulty>3 or difficulty<1:
  print("Difficulty Level 1-3: ")
  difficulty = int(input())

max_number = difficulty*25

#game 1
while games_number <= max_games:
  print("Game " + str(games_number))
  randomNumber = random.randint(0,max_number)
  currentChance = 1
  while currentChance<chances:
    print("Guess a Number Between 0 and " + str(max_number) + ": ")
    guess = int(input())
    if(guess == randomNumber):
     print("You Guessed Correctly")
     score.append("W")
     break;
    elif(guess < randomNumber):
     print("You Guessed Lower Than the Number")
    elif(guess > randomNumber):
     print("You Guessed Higher Than the Number")
    if(currentChance == 5):
     print("You Lost! The number was " + str(randomNumber))  
  score.append("L")
currentChance += 1
games_number += 1
print(*score)
