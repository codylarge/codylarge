import random

# List of words for the Hangman game
WORD_LIST = [
    "Future", "Picnic", "Agonistic", "Garland", "Protect", "Airline", "Gigantic", "Publish",
    "Bandit", "Goofy", "Quadrangle", "Banquet", "Government", "Recount", "Binoculars",
    "Grandkids", "Biologist", "Handbook", "Reflection", "Blackboard", "Vineyard", "Teamwork",
    "Himself", "Reporter", "Board", "Indulge", "Ring", "Bookworm", "Inflatable", "Salesclerk",
    "Butterscotch", "Inmate", "Snapshot", "Camera", "Intern", "Shellfish", "Campus", "Eyewitness", 
    "Invest", "Ship", "Catfish", "Jackpot", "Significance", "Carsick", "Sometimes", "Nearby", 
    "Celebrate", "Lawyer", "Sublime", "Celery", "Life", "Tabletop", "Citizen", "Lifeline", 
    "Coloring", "Love", "Tennis", "Compact", "Magnificent", "Timesaving", "Dark", "Tree", "Wealth",
    "Damage", "Man", "Termination", "Dangerous", "Mascot", "Underestimate", "Marshmallow", 
    "Endorse", "Mine", "Moonwalk", "Way", "Erratic", "Envelope", "Wednesday", "Newborn", "World", 
    "Eulogy", "Fish", "Parenthesis", "Zestful", "Food", "Perpetrator", "Foreclose", "Phone"
]

# Initialize game state variables
target_word = ""
current_word = ""
incorrect_guesses = []

def select_random_word():
    return random.choice(WORD_LIST)

def initialize_game():
    global target_word, current_word, incorrect_guesses
    target_word = select_random_word()
    current_word = "_" * len(target_word)
    incorrect_guesses = []

# Check the guessed letter
def check_guess(letter):
    global current_word, incorrect_guesses
    if letter in target_word:
        # Update current_word with correctly guessed letter(s)
        for i in range(len(target_word)):
            if target_word[i] == letter:
                current_word = current_word[:i] + letter + current_word[i + 1:]
    else:
        # Add incorrect guess to the list
        incorrect_guesses.append(letter)

# Function to update README.md with the current game state
def update_readme():
    with open('README.md', 'w') as readme:
        # Update the README.md content with the game state
        readme.write(f'### Hangman Game\n\n')
        readme.write(f'Current Word: {current_word}\n')
        readme.write(f'Incorrect Guesses: {", ".join(incorrect_guesses)}\n')

if __name__ == "__main__":
    initialize_game()
    update_readme()
