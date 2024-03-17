
def printSth(word,color):
  if color == "purple":
    print("\033[35m", word, sep="", end="")
  elif color == "red":
    print("\033[31m", word, sep="", end="")
  elif color == "green":
    print("\033[32m", word, sep="", end="")
  elif color == "reset":
    print("\033[0m", word, sep="", end="")


print("Super Subroutine")
print("With my ", end="")
printSth("new program ", "purple")
printSth("I can just call red('and') ", "reset")
printSth("and ", "red")
printSth("that word will appear in the color I set it to.", "reset")
print()
print()
printSth("With no ", "reset")
printSth("weird gaps", "green")
printSth(".", "reset")
print()
print()
printSth("Epic.", "reset")
