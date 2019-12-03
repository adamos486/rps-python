import unittest
from RPS import RPS, ROCK, PAPER, SCISSORS


class TestRPS(unittest.TestCase):
    def test_play_returns_something(self):
        game = RPS()
        result = game.play(ROCK, PAPER)
        self.assertIsNotNone(result)

    def test_when_player1_is_rock_and_player2_is_paper_then_player2_wins(self):
        game = RPS()
        result = game.play(ROCK, PAPER)
        self.assertEqual("Player 2 Wins", result)

    def test_when_player1_is_paper_and_player2_is_rock_then_player1_wins(self):
        game = RPS()
        result = game.play(PAPER, ROCK)
        self.assertEqual("Player 1 Wins", result)

    def test_when_player1_is_scissor_and_player2_is_paper_then_player1_wins(self):
        game = RPS()
        result = game.play(SCISSORS, PAPER)
        self.assertEqual('Player 1 Wins', result)

    def test_when_player1_is_paper_and_player2_is_scissor_then_player2_wins(self):
        game = RPS()
        result = game.play(PAPER, SCISSORS)
        self.assertEqual('Player 2 Wins', result)

    def test_when_player1_is_rock_and_player2_is_scissors_then_player1_wins(self):
        game = RPS()
        result = game.play(ROCK, SCISSORS)
        self.assertEqual('Player 1 Wins', result)

    def test_when_player1_is_scissors_and_player2_is_rock_then_player2_wins(self):
        game = RPS()
        result = game.play(SCISSORS, ROCK)
        self.assertEqual('Player 2 Wins', result)

    def test_when_player1_and_player2_throw_the_same_then_tie(self):
        game = RPS()
        result = game.play(ROCK, ROCK)
        self.assertEqual('Player 1 and 2 Tie', result)

        result = game.play(PAPER, PAPER)
        self.assertEqual('Player 1 and 2 Tie', result)

        result = game.play(SCISSORS, SCISSORS)
        self.assertEqual('Player 1 and 2 Tie', result)
