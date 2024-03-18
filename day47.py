import time, os,random

def generate_stats():
  return random.randint(-1000,1000)

def computerFighter(card,stat):
  categorien=["Sailor Moon","Freeza","Kaito Kid","Piccolo"]
  compStat = random.choice(categorien)
  compStatValue = categories[categorien.index(compStat)]["stat"][stat_input_mapping[stat]]
  #print(compStat)
  #print(categorien.index(compStat)+1)
  if compStat != categorien[int(card) - 1]:
     return compStat,compStatValue
  else:
    return computerFighter(card,stat)
  
    
print("🌟 Welcome to Top Trump 🌟")
print()
score_player= 0
score_comp= 0
while True: 
  card = input("Choose your card:\n1 - Sailor Moon\n2 - Freeza\n3 - Kaito Kid\n4 - Piccolo\n >")
  categories = [
      {
        "name": "Sailor Moon",
        "stat": {
          "Strength": generate_stats(),
          "Speed": generate_stats(),
          "Intelligence": generate_stats(),
          "Fighting": generate_stats()
          }
      },
      {
        "name":"Freeza",
        "stat": {
            "Strength": generate_stats(),
            "Speed": generate_stats(),
            "Intelligence": generate_stats(),
            "Fighting": generate_stats()
        }
      },
      {
        "name":"Kaito Kid",
        "stat": {
            "Strength": generate_stats(),
            "Speed": generate_stats(),
            "Intelligence": generate_stats(),
            "Fighting": generate_stats()
        }
      },
      {
        "name":"Piccolo",
        "stat": {
            "Strength": generate_stats(),
            "Speed": generate_stats(),
            "Intelligence": generate_stats(),
            "Fighting": generate_stats()
        }
      }
  ]
  print()
  print(f"You have chosen {categories[int(card) -1]['name']}")
  print()
  # computerFighter(card)
  
  stat = input("Choose your stat:\n1 - Strength\n2 - Speed\n3 - Intelligence\n4 - Fighting\n> ")
  print()
  stat_input_mapping = {
      "1": "Strength",
      "2": "Speed",
      "3": "Intelligence",
      "4": "Fighting"
  }
  com_cardName, com_cardStat = computerFighter(card,stat)
  print(f"You will fight with {com_cardName}")
  print()
  if stat in stat_input_mapping:
    # Get the corresponding statistic name
    cardName=categories[int(card)-1]["name"]
    stat_name = stat_input_mapping[stat]
    cardStatName = stat_name
    cardStat = categories[int(card)-1]["stat"][stat_name]
    #print(f"{cardName} has a {cardStatName} of {cardStat}")
    time.sleep(2)
    print(f"{cardName} has a {cardStatName} of {cardStat}")
    print(f"{com_cardName} has a {cardStatName} of {com_cardStat}")
    print()
    print("\033[33m")

    if cardStat > com_cardStat:
      print(f"***************{cardName} wins!*************") 
      score_player += 1
    elif cardStat < com_cardStat:
      print(f"***************{com_cardName} wins!*************")
      score_comp += 1
    else:
      print("***************It's a tie!*************")
    print(f"\033[35m\n your score is {score_player}\n computer score is {score_comp}")
  else: 
    print("\033[31m")
    print("Invalid input. Please enter a number between 1 and 4.")
  
  print("\033[0m")
  
  again = input("Again? y/n > ")
  if again.lower()=="y":
    continue
  else:
    print("Thanks for playing!")
    time.sleep(2)
    os.system("clear")
    break
  

