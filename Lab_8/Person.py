from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax
import random

class LastCoin(TwoPlayerGame):
    def __init__(self, players):
        self.players = players 
        self.nplayers = len(players)  
        self.num_coins = 25  
        self.max_coins = 4  
        self.current_player = 1  

    def possible_moves(self):
        return [str(x) for x in range(1, min(self.max_coins, self.num_coins) + 1)]

    def make_move(self, move):
        self.num_coins -= int(move)

    def win(self):
        return self.num_coins == 0 

    def is_over(self):
        return self.win()  

    def scoring(self):
        return -100 if self.win() else 0  
    def show(self):
        print(self.num_coins, 'coins left in the pile')

def main():
    
    num_players = random.randint(3, 5)
    print(f"So nguoi choi trong van nay: {num_players}") 

    
    players = [Human_Player()] + [AI_Player(Negamax(13)) for _ in range(num_players - 1)]
    
   
    game = LastCoin(players)
    
    
    while not game.is_over():
        game.play()  
    
    
    if game.current_player - 1 > 0:
        print("Nguoi thang la Nguoi choi") 
    else:
        print("Nguoi thang la May") 

if __name__ == "__main__":
    main()
