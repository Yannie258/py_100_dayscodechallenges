import random, time, os
def generatorGame():
    round = 0
    
    name1 = input("Name your Legend: \n")
    character1 = input("Character Type (Human, Elf, Wizard, Orc): \n")
    time.sleep(1)
    print(name1)
    time.sleep(1)
    health1 = health()
    print("HEALTH: ", health1 )
    time.sleep(1)
    strength1= strength()
    time.sleep(1)
    print("STRENGTH: ", strength1)
    print("Who are they battling?")
    
    time.sleep(1)

    name2 = input("Name your Legend: \n")
    character2 = input("Character Type (Human, Elf, Wizard, Orc): \n")
    print(name2)
    time.sleep(1)
    health2=health()
    print("HEALTH: ", health2) 
    time.sleep(1)
    strength2=strength()
    print("STRENGTH: ", strength2)
    
    os.system("clear")

    beginBattle(name1,health1, strength1, name2,health2,strength2)
    

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

def beginBattle(name1,health1, strength1,name2,health2,strength2):
    print("⚔️ BATTLE TIME ⚔️")
    print()
    print("The battle begins!")
    round=0
    
    while True:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        if dice1 > dice2:
            print(name1, "wins the first blow")
            print(name2, "takes a hit, with", abs(strength1-strength2), "damage")

            health2 = health2 - abs(strength1-strength2)
            print(name1)
            print("HEALTH: ", health1)
            print(name2)
            print("HEALTH: ", health2)
        elif dice1 < dice2:
            print(name2, "wins the first blow")
            print(name1, "takes a hit, with", abs(strength2-strength1), "damage")

            health1 = health1 - abs(strength2-strength1)
            print(name1)
            print("HEALTH: ", health1)
            print(name2)
            print("HEALTH: ", health2)
        else:
            print(name1, "ties")
        
        round +=1
        time.sleep(1)
        if health1 <= 0:
            print(name1, "has died!")
            print(name2, "destroyed", name1, "in", round, "rounds!")
            break
        elif health2 <= 0:
            print(name2, "has died!")
            print(name1, "destroyed", name2, "in", round, "rounds!")
            break
        else:
            print("And they're both standing for the next round!")
            time.sleep(1)
            os.system("clear")
            print("⚔️ BATTLE TIME ⚔️")
            print()
            print("The battle continues!")
            continue

generatorGame()