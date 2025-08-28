import random

class CandyGame:
    def __init__(self, total_candies):
        self.total_candies = total_candies
        self.max_candies_per_turn = 20
        self.current_player = "Human"  

    def switch_player(self):
        self.current_player = "AI" if self.current_player == "Human" else "Human"

    def player_move(self):
        
        try:
            candies_taken = int(input(f"{self.current_player}, vui long nhap so keo ban muon lay (1-20): "))
            if 1 <= candies_taken <= self.max_candies_per_turn:
                self.total_candies -= candies_taken
                print(f"{self.current_player} lay {candies_taken} vien keo. Con lai {self.total_candies} vien keo.")
            else:
                print("So keo khong hop le! Vui long chon tu 1 den 20.")
                self.player_move() 
        except ValueError:
            print("Vui long nhap mot so!")
            self.player_move()

    def ai_move(self):
        candies_taken = random.randint(1, self.max_candies_per_turn)  
        if candies_taken > self.total_candies:
            candies_taken = self.total_candies
        self.total_candies -= candies_taken
        print(f"AI lay {candies_taken} vien keo. Con lai {self.total_candies} vien keo.")

    def check_winner(self):
        if self.total_candies <= 0:
            if self.current_player == "Human":
                print("Nguoi choi da nhan vien keo cuoi cung. May thang!")
            else:
                print("May da nhan vien keo cuoi cung. Nguoi choi thang!")
            return True
        return False

    def play_game(self):
        print("Tro choi keo bat dau!")
        print(f"So keo ban dau trong lo: {self.total_candies}")

        while self.total_candies > 0:
            if self.current_player == "Human":
                self.player_move()  
            else:
                self.ai_move() 

            if self.check_winner():
                break
            
            self.switch_player() 

if __name__ == "__main__":
  
    game = CandyGame(1000)
    game.play_game()
