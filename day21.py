print("Match Game!")
mul = int(input("Name your multiples: "))

score = 0
for i in range(1, 11):
  print(i, "x", mul, "=")
  ans = int(input())
  if ans == i * mul:
    print("Great work!")
    score += 1
  else:
    print("Nope. The answer was", i * mul)

print("--------------")
print("You scored", score, "out of 10.")
