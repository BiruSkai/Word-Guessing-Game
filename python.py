import random, math

# Greeting
print("Welcome to my Word Game.")

# List of words
words = ["bag", "bird", "drink", "mouse", "pizza", "vegetable", "wall", "plane", "finger", "eel"]

# List for random word
display = []

#Getting random word from the list
randomIndex = math.floor(random.random() * len(words))
randomWord = words[randomIndex]

# Number of letter of random word
lengthRandom = len(randomWord)

# Number of guessing
chance = lengthRandom + math.ceil(lengthRandom / 2)
print(f"You have {chance} chances for guessing in this game.")

# Set "_" into display depending on random word
for i in range(lengthRandom):
        display.append("_")

# Condition at start
print(f"EmptyLetter at start: {lengthRandom}")
print(display)

# Var for query() function
emptyLetter = lengthRandom

# Inserting correct user letter to display
def query():
        global emptyLetter, lengthRandom, randomWord

        userLetter = input("Type a letter: ").lower()
        
        for i in range(lengthRandom):
                if randomWord[i] == userLetter:
                        display[i] = userLetter
                        emptyLetter -= 1

        print(f"EmptyLetter after loop: {emptyLetter}")

        # Game won
        if emptyLetter == 0:
                print(display)
                print("Congratulations.")
        

# Start the program
query()
                
# Looping into query function until game completed
while emptyLetter > 0:
        print(display)
        chance -= 1

        if chance > 0 and emptyLetter > 0:
                print(f"You have {chance} chances to guess.")
                query()

        elif chance == 0:
                print("You lose the game.")
                break                





        

