beastDic={}
beastList=[]
def pretty_print():
  for beast_dic in beastList:
    type= beast_dic['characters']['element'].title()
    if type == "Earth":
      print("\033[32m", end="") #green
    elif type == "Fire":
      print("\033[31m", end="") #red
    elif type == "Air":
      print("\033[37m", end="") #grey
    elif type == "Water":
      print("\033[34m", end="") # blue
    elif type == "Spirit":
      print("\033[35m", end="") #magenta

    print(f"name: {beast_dic['name']}", end=" | ")
    for subkey, subvalue in beast_dic["characters"].items():
      print(f"{subkey}: {subvalue}", end=" | ")

    print()

while True: 
  print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")
  print()
  name = input("Input your beast's name > ")
  print()
  element = input("Input your beast's type > ")
  print()
  move = input("Input your beast's special move > ")
  print()
  hp = input("Input your beast's starting HP > ")
  print()
  mp = input("Input your beast's starting MP > ")
  print()
  beastDic = {"name":name} 
  characters = {"element":element, "special move":move, "HP":hp, "MP":mp}
  beastDic["characters"] = characters
  print(beastDic) # 2D dictionary
  beastList.append(beastDic)
  #print(beastList)
  again = input("Again? y/n > ")
  if again.lower() == 'y':
    continue
  else:
    pretty_print()
    break
  print()
  