"""
- user inputs  name of  the test
- user inputs max score
- user inputs score they can receive
- program calculates the percentage
- program returns the grade
- emotional support
"""

test=input("What is the name of the test? ")
max_score=int(input("What is the max score? "))
score=int(input("What is your score? "))
percentage=round(score/max_score*100,2)
if percentage>=90:
  print("You got an A+")
elif percentage>=80:
  print("You got an A")
elif percentage>=70:
  print("You got a B")
elif percentage>=60:
  print("You got a C")
elif percentage>=50:
  print("You got a D")
else:
  print("You got a U")