import texts
import random
import os
os.system('cls' if os.name=='nt' else 'clear')
class Player:
    def __init__(self):
        self.name = ''
        self.life = 6


class Game:
    def __init__(self, player):
        self.guess_list = []
        self.talalt = 0
        self.player = player
        self.game_running = False
        self.word = ''
        self.hidden = ''
        self.bottom_range = 0
        self.top_range = len(texts.word_list) -1
        print( texts.greet_text["welcome"] )
        print( texts.greet_text["game_rules"].format(self.player.life) )
        print( texts.greet_text["name_add"]  )
        self.player.name = input()
        self.start_game()

    def start_game(self):
        self.guess_list = []
        self.hidden = ''
        self.player.life = 6
        self.game_running = True
        self.word = texts.word_list[random.randint(self.bottom_range, self.top_range)]
        self.hidden +='*'*len(self.word)
        print(texts.greet_text['greet_player'].format(self.player.name))
        self.game_loop()

    def game_loop(self):
        while self.game_running:
            self.hangman_draw()
            print('You already guessed: ', self.guess_list,'\n')
            print('Life remaining: ', self.player.life, '\n')
            print(self.hidden)
            if self.player.life <= 0:
                print(texts.game_loop['lost'])
                self.game_running = False
                self.restart_game()
            else:
                self.letter_guess()

    def letter_swap(self, number):
        self.guess_list.append(number)
        print('You already guessed: ', self.guess_list)
        self.hidden = list(self.hidden)
        self.word = list(self.word)
        for i in range(len(self.word)):
            if number == self.word[i]:
                self.hidden[i] = self.word[i]
                self.talalt += 1
        if self.talalt < 1 :
            self.player.life -= 1
            print(texts.guessing['wrong'].format(self.player.life))


    def letter_guess(self):
        self.talalt = 0
        if self.hidden == self.word:
            print(texts.game_loop["you_won"].format(self.player.name))
            self.game_running = False
            self.restart_game()
        else:
            guess = str(input(texts.guessing["aguess"]))
            guess = guess.upper()
            if guess in self.guess_list:
                print(texts.game_loop['already_letter'].format(guess))
            else:
                self.letter_swap(guess)
            self.hidden = ''.join(self.hidden)
            self.word = ''.join(self.word)

    def hangman_draw(self):
        os.system('cls' if os.name=='nt' else 'clear')
        if self.player.life == 6:
            print("________      ")
            print("|      |      ")
            print("|             ")
            print("|             ")
            print("|             ")
            print("|             ")
        elif self.player.life == 5:
            print( "________      ")
            print( "|      |      ")
            print( "|      0      ")
            print( "|             ")
            print( "|             ")
            print( "|             ")
        elif self.player.life == 4:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /       ")
            print("|             ")
            print("|             ")
        elif self.player.life == 3:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|      ")
            print("|             ")
            print("|             ")
        elif self.player.life == 2:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|             ")
            print("|             ")
        elif self.player.life == 1:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     /       ")
            print("|             ")
        elif self.player.life == 0:
            print ("________      ")
            print ("|      |      GAME ")
            print ("|      0        OVER!")
            print ("|     /|\     ")
            print ("|     / \     ")
            print ("|             ")



    def restart_game(self):
        while not self.game_running:
            print(texts.game_loop['new_game'])
            answer = str(input('(Y)es or (N)o?'))
            if answer.lower() == 'y':
                self.start_game()
            elif answer.lower() == 'n':
                print('Bye then')
                break # END OF GAME
            else:
                print("Say Yes or No you fag!")





player = Player()
hangman_game = Game( player )
