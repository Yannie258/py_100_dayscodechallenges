import random 
def roll_a_dice(num_dice):
  dice = random.randint(1,num_dice)
  return dice

def health():
  dice_6 =roll_a_dice(6)
  dice_8 = roll_a_dice(8)
  cal_health = dice_6 * dice_8
  return cal_health

def game():
  print("Character Stats Generator")
  while True:
    print()
    name = input("Name your warrior: ")   
    if name == "exit":
      break
    else:
      print("Their health is: \033[1;32m",health() ,"hp")

game()
  
