import random

print("Totally Random One-Million-to-One")
numb = random.randint(1,1000000)
print(numb)
attemp = 0
while True:
  attemp +=1 
  guest = int(input("what is your guest? "))
  if guest < 0:
    exit()
  if guest == numb:
    print("Correct! you win after try", attemp,"times")
    break
  elif guest > numb:
    print("too high")
  else:
    print("too low")
   
