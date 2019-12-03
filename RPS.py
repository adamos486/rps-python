PAPER = 'PAPER'
ROCK = 'ROCK'
SCISSORS = 'SCISSORS'


class RPS:
    def __init__(self):
        self.something = "RPS"
        print("init RPS")

    def play(self, play1, play2):
        print("something:", self.something)
        print("play1:", play1, "play2:", play2)
        if play1 == ROCK:
            if play2 == ROCK:
                return 'Player 1 and 2 Tie'
            elif play2 == SCISSORS:
                return 'Player 1 Wins'
            elif play2 == PAPER:
                return 'Player 2 Wins'
        elif play1 == PAPER:
            if play2 == PAPER:
                return 'Player 1 and 2 Tie'
            elif play2 == ROCK:
                return 'Player 1 Wins'
            elif play2 == SCISSORS:
                return 'Player 2 Wins'
        elif play1 == SCISSORS:
            if play2 == SCISSORS:
                return 'Player 1 and 2 Tie'
            elif play2 == ROCK:
                return 'Player 2 Wins'
            elif play2 == PAPER:
                return 'Player 1 Wins'
