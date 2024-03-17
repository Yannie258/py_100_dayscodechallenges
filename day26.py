import pygame

import os, time

def play():
  pygame.init()
  mySound= pygame.mixer.Sound("./testSound.mp3")
  mySound.play()
  playSound = True

  while True:
    # Start taking user input and doing something with it
    
    user=input()
    if user=="p" and playSound == True:
      pygame.mixer.pause()
      playSound = False
      continue
    elif user=="q":
      exit()
    else:
      pygame.mixer.unpause()
      playSound = True
      

while True:
  # clear the screen 
  os.system("clear")
  # Show the menu
  print("🎵 MyPOD Music Player")
  time.sleep(1)
  print("Press 1 to Play")
  time.sleep(1)
  print("Press 2 to Exit")

  # take user's input
  userInput = int(input())

  # check whether you should call the play() subroutine depending on user's input
  if userInput == 1:
    play()
  elif userInput == 2:
    exit()
  else:
    continue