import random

word_list = [
    "aardvark", "baboon", "camel", "elephant", "giraffe", "hippopotamus", "kangaroo", "leopard",
    "mongoose", "narwhal", "octopus", "penguin", "quokka", "rhinoceros", "squirrel", "tiger",
    "umbrella", "vulture", "walrus", "xenopus", "yak", "zebra", "airplane", "bicycle", "computer",
    "dinosaur", "education", "friendship", "guitar", "happiness", "imagination", "jellyfish",
    "keyboard", "lighthouse", "mountain", "notebook", "observatory", "painting", "question",
    "rainbow", "sunshine", "telescope", "universe", "vacation", "waterfall", "xylophone",
    "yesterday", "zeppelin", "adventure", "butterfly", "celebration", "discovery", "envelope",
    "festival", "garden", "harmony", "innovation", "journey", "knowledge", "laughter", "melody",
    "nature", "opportunity", "paradise", "quality", "research", "serenity", "tradition",
    "understanding", "volunteer", "wisdom", "excellence", "yogurt", "zucchini", "astronomy",
    "bakery", "chocolate", "drumstick", "escalator", "firefighter", "gymnasium", "hedgehog",
    "illustration", "jackrabbit", "kaleidoscope", "laboratory", "microscope", "nightingale",
    "orchestral", "photograph", "quicksand", "restaurant", "skateboard", "thunderstorm",
    "underground", "volleyball", "windmill", "xylograph", "yesterday", "zookeeper", "appliance",
    "blueprint", "clockwork", "dashboard", "equipment", "framework", "goldfish", "handshake",
    "iceberg", "jukebox"
]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
word_length = len(chosen_word)
for i in range(word_length):
    placeholder += "_"
print(placeholder)

# Keep track of all correct guesses
correct_letters = []

# TODO-1: Use a while loop to let the user guess again
# The loop should only stop once the user has guessed all the letters
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # TODO-2: Update the for loop so that previous guesses are added to the display
    # Check if the guess is in the word and add to correct_letters if it is
    if guess in chosen_word:
        correct_letters.append(guess)

    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    # Check if user has won (no more blanks)
    if "_" not in display:
        end_of_game = True
        print("****You Win!****")