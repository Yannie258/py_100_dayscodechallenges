import random 
def roll_dice():
  while True:
    print("Infinity dice  🎲")
    sides = int(input("How many sides?: "))
    roll = random.randint(1, sides)
    print("You rolled", roll)
    again = input("Roll again? ")
    if again == "yes":
      continue
    else:
      break
  print("thanks for playing! ")

roll_dice()