import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  counter = 1 
  for order in listOfEmail: 
    print(f"{counter}: {order}") 
    counter += 1 
  time.sleep(1)
  os.system("clear")

def spam(emails):
  for i in range(0,emails): # 10 emails
    print()
    print(f"Email {i+1}")
    print()
    print(f"Dear {listOfEmail[i]}")
    print("It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.")
    print()
    print("Love and hugs,")
    print("Ian Spammington III")
    time.sleep(3)
    os.system("clear")
  
while True:
  print("Spammer Inc.")
  menu = input("1. add email \n2: Delete email\n3. view emails\n4. spamming\n> ")
  if menu == "1":
    order = input("email > ")
    listOfEmail.append(order)
    prettyPrint()
  elif menu =="2":
    order = input ("delete email> ")
    if order in listOfEmail:
      listOfEmail.remove(order)
    else:
      print("no email found")
    prettyPrint()
  elif menu == "3": 
    prettyPrint() 
  elif menu == "4":
    spam(len(listOfEmail))
  time.sleep(1)
