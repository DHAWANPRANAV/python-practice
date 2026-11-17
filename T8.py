#Create a small program that asks for a user's first name, last name, and year of birth. 
#Calculate their approximate age and print their full name with age.




from datetime import datetime  # Importing datetime from the built-in module

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = int(input("Enter your year of birth: "))

current_year = datetime.now().year
age = current_year - birth_year

print("Full Name:", first_name, last_name)
print("Your Approximate Age:", age)
