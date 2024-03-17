import random,sys
print("🌟Hangman🌟")
guess_word_list = ["python","java", "kotlin","javascript","typescript","ruby"]
guess_word=random.choice(guess_word_list)
used_word =[]
count=6
while True:
  letter = input("\nChoose a letter: ")
  if letter not in guess_word:
    print("Nope, not in there.")
    print()
    count -=1
    if count < 0:
      print("You lost! ")
      break
    else:
      print(f"{count} left")
      continue
  else:
    print("\nCorrect!\n")
    used_word.append(letter)   
    for i in guess_word:      
      if i in used_word:
        print(i,end="")
      else:
        print("_", end="")
      if len(used_word) != len(guess_word):
        continue
      else:
        print(f"Yes, the answer is: {guess_word}")
        print(f"you won with {count} lives left")
        sys.exit()
        
  
  
    
    
    
    
