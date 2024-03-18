import time, os
def inputUser():
  text = input(">")
  return text
  
while True:
  print("Input your 3 letters and score out of 100,000: >")
  user= inputUser()
  userInputs = user.split()
  if len(userInputs) > 3 or len(userInputs) <2:
    print("please input 2 arguments with space between")
    time.sleep(2)
    os.system("clear")
    
    continue
  letter= userInputs[0]
  score=int(userInputs[1])
  if len(letter) > 3:
    print("Error: Too many letters")
    continue
  elif len(letter) < 3:
    print("Error: Too few letters")
    continue

  if score > 100000:
    print("Error: Too high of a score")
    continue
  elif score < 0:
    print("Error: Too low of a score")
    continue
  print("Initials: ", letter)
  print("Score: ", score)
  f = open("high.score", "a+")
  f.write(f"{user}\n")
  f.close()
  print()
  print("Added to high score table.")
  print()
  print("Add another? y/n")

  ask = inputUser()
  if ask == "y":
    continue
  else:
    break
  