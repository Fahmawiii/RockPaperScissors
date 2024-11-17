import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass
    
class Rockplayer(Player):
    def move(self):
        return 'rock'
    
class Randomplayer(Player):
    def move(self):
        return random.choice(moves)
    
class Humanplayer(Player):
    def move(self):
        human_move = input("Rock, Paper, or Scissors?\n").lower()
        if human_move in moves:
            return human_move
        else:
            print("please type in Rock, Paper, or Scissors")
            return self.move()
        
class Reflectplayer(Player):
    def __init__(self):
        self.their_move = None

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move
    
class CyclePlayer(Player):
    def __init__(self):
        self.my_move = None

    def learn(self, my_move, their_move):
        self.my_move = my_move

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        if self.my_move == 'rock':
            return 'paper'
        if self.my_move == 'paper':
            return 'scissors'
        if self.my_move == 'scissors':
            return 'rock'
        
    
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

def mode():
    """Main menu to select game mode."""
    while True:
        game_mode = input(
            "Please select a game mode (starter, easy, medium, hard) or type exit to quit:\n"
        ).lower()

        if game_mode == 'starter':
            print("Starter Mode Selected")
            game = Game(Humanplayer(), Rockplayer())
        elif game_mode == 'easy':
            print("Easy Mode Selected")
            game = Game(Humanplayer(), Randomplayer())
        elif game_mode == 'medium':
            print("Medium Mode Selected")
            game = Game(Humanplayer(), Reflectplayer())
        elif game_mode == 'hard':
            print("Hard Mode Selected")
            game = Game(Humanplayer(), CyclePlayer())
        elif game_mode == 'exit':
            print("Thanks for playing!")
            break
        else:
            print("Invalid mode. Please type in starter, easy, medium, hard, or exit.")
            continue
        
        game.play_game()
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no):\n").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break


class Game:
    
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
       """"plays a single round of the game."""
       print(f"Player 1 score:{self.p1_score}")
       print(f"Player 2 score:{self.p2_score}")
       move1 =  self.p1.move()
       move2 =  self.p2.move()
       print(f"player 1:{move1} player 2:{move2}")

       if move1 == move2:
           print("Game Tied!!")
       elif beats(move1,move2):
           self.p1_score += 1
           print("Player 1 wins the round!")
       else:
           self.p2_score += 1
           print("Player 2 wins the round!")

       self.p2.learn(move2,move1)
       
    def play_game(self):
        """ Plays full 3 rounds"""
        print("Game start!")
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        self.result()
        print("Game over!")

    def result(self):
        """show the final result of the game"""
        print(f"final score for player 1: {self.p1_score}")
        print(f"final score for player 2:{self.p2_score}")

        if self.p1_score == self.p2_score:
            print("No winner! its a draw")
        elif self.p1_score < self.p2_score:
            print("player 2 wins the game")
        else:
            print("player 1 wins the game!")

if __name__ == '__main__':
   print("Welcome To Play Rock Paper Scissors")
   print("Type Starter, Easy, Medium, or Hard to Begin!\nType Exit to quit")
   mode()

