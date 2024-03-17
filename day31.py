def change_color(text, color, alignment):
  if color == "red":
      print(f"\033[31m{text:{alignment}}\033[0m", end="")
  elif color == "green":
      print(f"\033[32m{text:{alignment}}\033[0m", end="")
  elif color == "blue":
      print(f"\033[34m{text:{alignment}}\033[0m", end="")
  elif color == "purple":
      print(f"\033[35m{text:{alignment}}\033[0m", end="")
  elif color =="yellow":
      print(f"\033[33m{text:{alignment}}\033[0m", end="")
  else:
      print(f"\033[0m{text:{alignment}}\033[0m", end="")

def interface1():
  change_color('', 'red', '<10')
  change_color("=", "red", "")
  change_color("=", "white", "")
  change_color("=", "blue", "")
  change_color(" Music App ", "white", "")
  change_color("=", "blue", "")
  change_color("=", "white", "")
  change_color("=", "red", "")
  print()
  print()
  print("🔥 ▶   Radio Gaga", end="\n")
  
  change_color("Queen", "yellow", ">12")
  print()
  print()
  print("\nPREV")
  change_color("NEXT", "green", ">10")
  print()
  change_color("PAUSE","purple",">20")

def interface2():
  change_color("WELCOME TO", "", "^40")
  print()
  change_color("--", "blue", ">10")
  change_color("ARMBOOK", "blue", "^20")
  change_color("--", "blue", ">3")
  print()
  change_color("Definitely not a rip off of", "yellow", ">35")
  print()
  change_color("a certain other social", "yellow", ">35")
  print()
  change_color("networking site.", "yellow", ">35")
  print()
  print()
  change_color("Honest.", "red", "^40")
  print()
  print()
  change_color("Username:", "white", "^40")
  print()
  change_color("Password:", "white", "^40")
  

interface1()
print()
print("------------------------------------------------------")
interface2()