import os, time

def printList():
  print() 
  for item in myTodoList:
    print(f"{'':>10}\033[35m {item}")
  print() 

myTodoList = []


while True:
  
  print("\033[0mTo Do List Manager:\n\n")
  time.sleep(1)
  todo = input("Do you want to view, add, or edit your to do list? \n")
  if todo == "add":
    time.sleep(1)
    item = input("Add your item: \n")
    myTodoList.append(item)
    time.sleep(1)
    os.system("clear")
    print("Todo:")
    printList()
  elif todo == "view":
    time.sleep(1)
    os.system("clear")
    print("Todo:")
    printList()
  elif todo == "edit":
    item = input("What do you want to remove? ")
    if item in myTodoList:
      myTodoList.remove(item)
      time.sleep(1)
      os.system("clear")
      print("Todo:")
      printList()
      
    else:
      print(f"{item} was not in the list")
  else:
      print("{todo} was not in available activity")
  