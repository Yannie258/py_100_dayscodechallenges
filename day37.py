print("🌟Star Wars Name Generator🌟")
# firstName = input("Input your first name > ")
# lastName = input("Input your lastname > ")
# maidenName = input("Input your mother's maiden name > ")
# city = input("Input the city where you were born > ")
# print(f"Your Star Wars name is {firstName[:3].title()}{lastName[:3].lower()}")
# print(f"{maidenName[:2].title()}{city[-3:].lower()}")

name= input("Input full name: ") #David Morgan
maidenName = input("Input your mother's maiden name > ")
#Leave the last argument blank. ex: [-5:] gets the last 5 characters.
city = input("Input the city where you were born > ")
print(f"Your Star Wars name is {name.split()[0][:3].title()}{name.split()[1] [:3].lower()} {maidenName[:2].title()}{city[-3:].lower()}") #Davmor Joiff



