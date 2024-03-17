myBill = float(input("What was the bill total?: "))
print("bill", myBill)
percentOfTip = int(input("How many tip?: "))
print("tip", percentOfTip)
total = myBill + myBill*percentOfTip/100
print("total", total)
numberOfPeople = int(input("How many people?: "))

answer = myBill / numberOfPeople
print("pro person :", answer)