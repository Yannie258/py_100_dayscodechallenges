
from getpass import getpass as input
player1_score = 0
player2_score = 0

print("Let's play chutes and ladders. Pick ladder or chute.")
while True:
#   print("E P I C    🪨  📄 ✂️    B A T T L E")
  print()
  print("Select your move (R, P or S)")
  print()
  player1Move = input("Player 1 > ")
  print()
  player2Move = input("Player 2 > ")
  print()

  if player1Move=="R":
    if player2Move=="R":
      print("You both picked Rock, draw!")
      continue
    elif player2Move=="S":
      player1_score +=1
      print("Player1 smashed Player2's Scissors into dust with their Rock!")

    elif player2Move=="P":
      player2_score +=1
      print("Player1's Rock is smothered by Player2's Paper!")
    else:
      print("Invalid Move Player 2!")
      continue


  elif player1Move=="P":
    if player2Move=="R":
      player1_score +=1
      print("Player2's Rock is smothered by Player1's Paper!")
    elif player2Move=="S":
      player2_score +=1
      print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
    elif player2Move=="P":
      print("Two bits of paper flap at each other. Dissapointing. Draw.")
      continue
    else:
      print("Invalid Move Player 2!")
      continue



  elif player1Move=="S":
    if player2Move=="R":
      player2_score +=1
      print("Player 2's Rock makes metal-dust out of Player1's Scissors")
    elif player2Move=="S":
      print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight")
      continue
    elif player2Move=="P":
      player1_score +=1
      print("Player1's Scissors make confetti out of Player2's paper!")
    else:
      print("Invalid Move Player 2!")
      continue


  else:
    print("Invalid Move Player 1!")
    continue

  print("player 1 scored: ", player1_score)
  print("player 2 scored: ", player2_score)
  if player1_score == 3 or player2_score == 3:
    if player1_score > player2_score:
      print("Player 1 wins!")
    else:
      print("Player 2 wins!")
    break
  
print("Thanks for playing!")


