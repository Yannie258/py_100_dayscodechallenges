import random, time
def generatorGame():
  while True:
    name = input("Name your Legend: ")
    character = input("Character Type (Human, Elf, Wizard, Orc): ")
    print(name)
    time.sleep(1)
    print("HEALTH: ", health()) 
    time.sleep(1)
    print("STRENGTH: ", strength())
    cont = input("Continue? ")
    if cont=="y":
       continue
    else:
       print("May your name go down in Legend...")
       break


def health():
  dice6=random.randint(1,6)
  dice8=random.randint(1,8)
  health = dice6*dice8/2 +10
  return health


def strength():
  dice6=random.randint(1,6)
  dice8=random.randint(1,8)
  strength = dice6*dice8/2 +12
  return strength


generatorGame()