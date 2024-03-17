print("🌟Website Rating🌟")
print()
website = {"name": None, "url": None, "description": None, "rating":None}
for key in website.keys():
  website[key] = input(f"input website {key}: ")

print()
for name, value in website.items():
  print(f"{name}: {value.strip()}")