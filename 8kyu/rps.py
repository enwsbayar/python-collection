# Rock Paper Scissors
# Let's play! You have to return which player won! In case of a draw return Draw!.

# Examples(Input1, Input2 --> Output):

# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"

def rps(p1, p2):
  return "Player 1 won!" if (p1 == "scissors" and p2 == "paper") or (p1 == "rock" and p2 == "scissors") or (p1 == "paper" and p2 == "rock") else "Player 2 won!" if p1 != p2 else "Draw!"

print(rps("scissors", "paper"))