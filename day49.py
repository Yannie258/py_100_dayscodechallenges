f = open("high.score", "r")
max_score= 0
leader=""
while True:
  contents=f.readline().strip()
  singleLine= contents.split()
  #print("Analyzing high score ...")
  if contents =="":
    break
  #print(int(singleLine[1]))
  score = int(singleLine[1])
  if score > max_score:
    max_score = score
    leader = singleLine[0]
    
  
print(f"Current leader is {leader} {max_score}")
f.close()
