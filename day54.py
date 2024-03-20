import csv # Imports the csv library

with open("Day54Totals.csv") as file: 
  reader = csv.DictReader(file) # use dictionary approach to load file
  total=0
  for row in reader: 
   # print (", ".join(row["Quantity"]))
    #print (row["Cost"])
    cost=float(row["Cost"])
    quantity=float(row["Quantity"])
    total += cost*quantity
       

print(f"Total: {total}")