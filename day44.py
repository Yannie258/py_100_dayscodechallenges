import random
initRandomList = []

def generateList():  
  list=[]
  while len(list) < 8:
    num = random.randint(0, 90)
    if num not in list:
          list.append(num)
  
  list.sort()  # Sort the list
  return list

def createCard(randomList):
  #print(randomList)
  bingoList=[
              [randomList[0],randomList[1],randomList[2]],
              [randomList[3],"BINGO",randomList[4]],
              [randomList[5],randomList[6],randomList[7]]
            ]
  for sublist in bingoList:    
    for i in range(len(sublist)):
      if i < len(sublist) - 1:
        print(f"{sublist[i]:^5}", end="\t|\t")
      else:
        print(sublist[i], sep="\t")
    print("------------------------------")


  #print(bingoList)
print("\033[33mBingo card generation")
print()
initRandomList = generateList()
while True: 
 #print(initRandomList)
 createCard(initRandomList)
 guess= int(input("Next number: ")) # compare in number , not a string because random int

 if guess in initRandomList:
   print("You have got it")
   index = initRandomList.index(guess)
   initRandomList[index] = 'x'
   
   #print(initRandomList)
   if initRandomList.count('x') == 8:
     print("You have won")
     break
 
   
   
  


