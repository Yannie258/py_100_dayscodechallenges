numb = 100
print(numb)
att = 0
while True:
  guest = int(input("guest a number"))
  if guest < 0:
    exit()
  if guest == numb:
    print("you win after try", att,"times")
    break
  elif guest > numb:
    print("too high")
  else:
    print("too low")
  att +=1  