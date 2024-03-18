def addIdea(idea):
  f = open("my.ideas", "a+")
  f.write(f"{idea}\n")
  f.close()

def showIdea():
  f = open("my.ideas", "r")
  while True:
    
    ideas = f.readline().strip()
    if ideas == "":
      break
    print(ideas)
  f.close()


print("****Idea Storage***")
while True:
  print()
  menu = input("Add an idea or see a random idea? a/r. > ")
  if menu == "a":
    print()
    idea = input("Input your idea. > \n")
    addIdea(idea)
    print()
    print("Nice! Your idea has been stored.")
    break
  elif menu == "r":
    showIdea()
    
  print()