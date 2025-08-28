from easyAI import TwoPlayerGame, solve_with_iterative_deepening, Human_Player, AI_Player, Negamax
from easyAI import TranspositionTable

class LastCoin(TwoPlayerGame):
    def __init__(self, players):
        self.players = players
        self.nplayer = 1  # Người chơi bắt đầu
        self.num_coins = 25
        self.max_coins = 4
        self.current_player = self.nplayer  # Khắc phục lỗi không tìm thấy `current_player`

    def possible_moves(self):
        return [str(x) for x in range(1, self.max_coins + 1)]

    def make_move(self, move):
        self.num_coins -= int(move)

    def win(self):
        return self.num_coins <= 0

    def is_over(self):
        return self.win()

    def scoring(self):
        return 100 if self.win() else 0

    def show(self):
        print(self.num_coins, 'coins left in the pile')

if __name__ == "__main__":
    tt = TranspositionTable()
    ai_algo = Negamax(13, tt)
    game = LastCoin([Human_Player(), AI_Player(ai_algo)])  # Truyền vào danh sách chứa hai người chơi
    game.play()

    r, d, m = solve_with_iterative_deepening(game, ai_depths=range(2, 20), win_score=100)
    print("Kết quả:", r)
    print("Độ sâu:", d)
    print("Nước đi:", m)

    if game.nplayer == 2:  # Người chơi AI là người chơi 2
        print('The winner is Machine')
    else:
        print('The winner is Human')
