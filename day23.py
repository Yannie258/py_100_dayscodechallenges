def loginSystem():
 print("Login System")
 print()
 while True:
   user = input("What is your username?: ")
   password = input("What is your password?: ")
   if user == "david" and password == "baldies4life":
     print("Welcome to Replit!")
     break
   else:
     print("Whoops! I don't recognize that username or password. Try again!")
     continue

loginSystem()
                    
                    

