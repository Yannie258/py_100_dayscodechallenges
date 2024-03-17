def pretty_print(type):
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

print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")
print()
beastDic = {"name":None, "type":None, "special_move":None, "starting_HP":None, "starting_MP":None}

for name in beastDic.keys():
  beastDic[name] = input(f"Input your beast's {name} > ").strip().title()
  print()
pretty_print(beastDic['type']) 
  # if beastDic['type'] == "Earth":
  #   print("\033[32m", end="") #green
  # elif beastDic['type'] == "Fire":
  #   print("\033[31m", end="") #red
  # elif beastDic['type'] == "Air":
  #   print("\033[37m", end="") #grey
  # elif beastDic['type'] == "Water":
  #   print("\033[34m", end="") # blue
  # elif beastDic['type'] == "Spirit":
  #   print("\033[35m", end="") #magenta
print(f"Your beast is called {beastDic['name']}. It is an {beastDic['type']} beast with a special move of {beastDic['special_move']}")
