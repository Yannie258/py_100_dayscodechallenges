import time, os
def add(name):
  order_list=[]
  while True: 
    print("How many Pizza's do you want?")
    try: 
     pizza = int(input("> "))
    except ValueError as err:
      print(err)
      print("Please enter a number")
      continue
    total_cost=0
  
    sizePizza = input("what size of pizza? (s,l,xl) > ")
    if sizePizza not in ['s','l','xl']:
        print("this size is not available")
        continue   
    item=[pizza,sizePizza]
    order_list.append(item)
    print(order_list)
    print(f"you ordered {pizza} pizzas of size {sizePizza}")
    again = input("Do you want to order more? (y/n) > ")
    if again == "y":
       continue
    else:
      break
    
  for order in order_list:
    print(order)
    total_cost += cost(order[0],order[1])

  print(f"Thanks {name}, your pizzas will cost {total_cost} $")
  return [name, order_list, total_cost]
    
def cost(pizzas,size):
  price = 0
  if size == "s":
    price = pizzas * 10
  elif size == "l":
    price = pizzas * 15
  elif size == "xl":
    price = pizzas * 20
  print(price)
  return price
       
def view(): 
  try: #auto load
    f=open("pizza.txt","r")
    data= f.readlines()
    for line in data:
      myEvent= eval(line)
      print(myEvent)
    f.close()
  except Exception as err:
    print("ERROR: Unable to load", err)

def autoSave(list):
  try:
    f=open("pizza.txt","a+")
    f.write(f"{str(list)}\n")
    f.close()
  except Exception as err:
    print("ERROR: Unable to save", err)


orderlist=[]
def main():
  print("***Dave's Dodgy Pizzas***")

  while True:
    
    print("1: Add Pizza\n2: View Pizzas\n3: Exit")
    menu = input("Enter your choice: ")
    if menu == "1":
      name = input("Name please > ")
      orderlist=add(name)
      autoSave(orderlist)
      break
      
    elif menu == "2":
      view()
      time.sleep(5)
      #os.system("clear")
      #continue
    elif menu == "3":
      break
    else:
      print("Invalid choice. Please try again.")
  
main()