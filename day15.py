
count = 0
while count < 10:
  animal = input("Enter an animal: ")
  print("My friend owns a", animal)
  if animal == "Cow":
    print("Moo")
  elif animal == "Cat":
    print("Meow")
  elif animal == "Dog":
    print("Woof")
  else:
    print("I don't know that animal")
    
  exit = input("Do you want to exit? ")
  if exit == "yes":
      break
    