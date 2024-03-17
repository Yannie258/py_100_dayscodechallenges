import os,sys,time
todoList=[]

def pretty_print(todoList):
  os.system("clear")
  print("To Do List")
  print()
  for index in range(len(todoList)):
    print(f"{index+1}: {todoList[index]}")
  time.sleep(1)

def addTodo():
  task = input(f"What is the task? > ")
  due = input(f"When is it due by? > ")
  priority = input(f"What is the priority? (high, medium or low)> ")
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


while True:
  print("🌟Life Organizer🌟")
  userInput = input("Welcome to the life organizer. Do you want to add, view, edit or remove a to do? > ")
  if userInput == "add":
    addTodo()

  elif userInput == "view":
    viewTodo(todoList)

  elif userInput == "edit":
    todo = input("What todo do you want to edit? > ")
    editTodo(todo)
  elif userInput == "remove":
    todo = input("What todo do you want to remove? > ")
    removeTodo(todo)
  command = input("Do you want to see the menu again or quit? >")
  if command == "quit":
    sys.exit()
  else:
    continue


