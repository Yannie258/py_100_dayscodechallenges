import time, os

def add_item():
  time.sleep(1)
  os.system("clear")
  print("INVENTORY")
  print("=========")
  print()
  item = input("Item to add > ").capitalize()
  inventory.append(item)
  print("Added")

def view():
  time.sleep(1)
  os.system("clear")
  print("INVENTORY")
  print("=========")
  print()
  #count item amount
  seen = []
  for item in inventory:
    if item not in seen:
      print(f"{item} {inventory.count(item)}")
      seen.append(item)

  time.sleep(2)

  
def remove_item(item):
  time.sleep(1)
  os.system("clear")
  print("INVENTORY")
  print("=========")
  print()
  item = input("Item to remove > ").capitalize()
  if item not in inventory:
    print("Item is not in inventory")
  else:
    for item in inventory:
      inventory.remove(item)
      print("Removed")
  

inventory = []

try:
  f = open("inventory.txt", "r")
  inventory = eval(f.read())
  f.close()
except:
  pass
  
while True:
  choose= input("1: Add 2: Remove 3: View >")
  if choose == "1":
    add_item()
  elif choose == "2":
    remove= input("What do you want to remove? >")
    remove_item(remove)
  elif choose == "3":
    view()
    
  try: 
    f = open("inventory.txt", "w")
    f.write(str(inventory))
    f.close()
  except Exception as err:
    print("Error", err)

    
    