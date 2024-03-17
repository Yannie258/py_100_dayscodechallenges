import time, os
listManager=[]

def print_pretty():
  os.system("clear")
  print("listManager:\n")
  for i in listManager:
    print(i)
  print()
  
while True:
  print("To do List Manager:\n")
  menu = input("Do you want to view, add, or edit your to do list?\n")
  if menu == "view":
    time.sleep(1)
    print_pretty()
  elif menu == "add":
    item = input("What do you want to add?\n")
    listManager.append(item)
  elif menu == "edit":
    item = input("What do you want to remove?\n")
    if item in listManager:
      verify=input("Are you sure you want to remove this?\n")
      if verify == "yes":
        listManager.remove(item)
        time.sleep(1)
        print("removed!")
      else:
        print("Okay, we won't remove it.")
    else:
      print(f"{item} was not in the list")
  time.sleep(3)
  os.system("clear")
  