import os,sys,time,random
todoList=[]
fileExists = True

try: 
  f = open("todo.txt","r")
  myEvents = eval(f.read())
  f.close()
except:
  print("ERROR: No existing calendar list, using a blank list")

def pretty_print(todoList):
  os.system("clear")
  print("To Do List")
  print()
  for index in range(len(todoList)):
    print(f"{index+1}: {todoList[index]}")
  time.sleep(1)

def addTodo():
  task = input("What is the task? > ")
  due = input("When is it due by? > ")
  priority = input("What is the priority? (high, medium or low)> ")
  row = [task, due, priority]
  todoList.append(row)
  print("Thanks, this task has been added.")

def removeTodo(todo):
  for row in todoList:
    if todo in row:
        todoList.remove(row)
        print("Task removed successfully.")
    else:
        print("Task not found.")


def viewTodo(list):
  view = input("1: View all\n2: View priority\n> ")
  if view == "1":
    pretty_print(list)
  else:
    priority = input("What priority? > ")
    for row in list:
      if priority in row:
        for item in row:
          print(item, end=" | ")
        print()
    print()
    time.sleep(1)

def editTodo(todo):
  edit = input("What do you want to edit? (task, due date, priority) > ")
  newTodo= input("What do you want to change it to? > ")
  for index in range(len(todoList)):
    if todo == todoList[index][0]:  # Checking the first element of each inner list
        if edit == "task":
            todoList[index][0] = newTodo
        elif edit == "due date":
            todoList[index][1] = newTodo
        elif edit == "priority":
            todoList[index][2] = newTodo
        print("Task edited successfully.")
    else:
        print("Task not found.")

def backup():
  time.sleep(1)
  os.system("clear")
  print("Previous task entries")
  f = open("todo.txt", "r")
  stuff = "".join(f.read())
  f.close()
  print((stuff))
  print()
  time.sleep(5)
  os.system("clear")
  

while True:
  print("🌟Life Organizer🌟")
  userInput = input("Welcome to the life organizer. Do you want to\n 1.add,\n 2.view,\n3.edit \4remove\n5. back-up a to do? > ")
  if userInput == "1":
    addTodo()

  elif userInput == "2":
    viewTodo(todoList)

  elif userInput == "3":
    todo = input("What todo do you want to edit? > ")
    editTodo(todo)
  elif userInput == "4":
    todo = input("What todo do you want to remove? > ")
    removeTodo(todo)
  elif userInput == "5":
    backup()

  if fileExists:
    try:
      os.mkdir("backups")
    except:
      pass
      
  #create random file name
  randx = random.randint(1, 1000000000)
  fname = f"backup{randx}.txt"

  os.popen(f"cp todo.txt backup/{fname}")

  f=open("todo.txt","a+")
  delist= ''.join(str(todoList))
  f.write(delist+ "\n")
  f.close()

  command = input("Do you want to see the menu again (any key) or quit (q)? >")
  if command == "q":
    exit()
  else:
    continue


