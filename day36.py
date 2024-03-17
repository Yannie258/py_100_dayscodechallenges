import os, time

nameList=[]

def pretty_print():
  os.system("clear")
  for i in nameList:
    print(i)

  time.sleep(1)
  

while True:
  firstName=input("First Name: ").strip().capitalize()
  lastName=input("Last Name: ").strip().capitalize()
  fullName=f"{firstName} {lastName}"
  if fullName not in nameList:
    nameList.append(fullName)
    time.sleep(2)
    pretty_print()
    
  else:
    print("ERROR: Duplicate name")
  time.sleep(1)
  os.system("clear")
    