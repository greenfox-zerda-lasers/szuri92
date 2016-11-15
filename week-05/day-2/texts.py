word_list = ['BEAVER', 'CASKET', 'MYSTICAL', 'GEAR', 'RESEARCH', 'PAINKILLER', 'COLORS', 'DESPAIR', 'COUPLE', 'PROGRAM']

greet_text = {
    'welcome': '\n>>>>>>>>>>>>>>>>>>>>Welcome to Hangman Game<<<<<<<<<<<<<<<<<<<<\n',
    'game_rules': "Every player starst with {0} health. You have to guess a random word. You can guess one letter each turn.\n If the word doesn't cointains the letter you lose 1 healt. If you reach 0 healt you DIE. If you can guess the word before you die, you won the Hangman Game!",
    'name_add': "First of all, give me your name, and let's begin",
    'greet_player': "Greetings {0}, now heres our random word, start guessing!\n\n"
}


game_loop = {
    'lost': 'You lost all your health, you died',
    'you_won': 'Congrats {0}, you guessed the word right',
    'new_game': 'Wanna play a new game?',
    'already_letter': '\nYou already gueesed {0}, give me an other letter!'
}

guessing = {
    'aguess': '\nGive me a letter\n\n',
    'right': 'Nice guess {0}, you still have {1} health.',
    'wrong': '\n\nWrong guess mortal, you lost 1 healt. You have {0} health remaining'
}
