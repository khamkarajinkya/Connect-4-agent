import board
import player
import random_player
import search
import random


def test_Q3():
  print("TESTING FOR Q3")
  b = board.Board()
  assert(search.find_win(b, 8) == "NO FORCED WIN IN 8 MOVES")
  b.make_move(2)
  b.make_move(0)
  b.make_move(3)
  b.make_move(0)
  assert(search.find_win(b, 3) == "WIN BY PLAYING 4")
  b.make_move(4)
  assert(search.find_win(b, 3) == "ALL MOVES LOSE")
  print("passed")


def test_Q4():
  players = [player.Player(),random_player.Player()]
  random.shuffle(players)
  print(players[0].name() + " vs " + players[1].name())

  b = board.Board()
  i = 0
  legal_moves = b.generate_moves()
  while not b.last_move_won() and len(legal_moves) > 0:
    move = players[i].get_move()
    players[0].make_move(move)
    players[1].make_move(move)
    b.make_move(move)
    i^=1
    legal_moves = b.generate_moves()
  if b.last_move_won():
    print("VICTORY FOR PLAYER " + players[i^1].name())
  else:
    print("DRAW")


test_Q4()

