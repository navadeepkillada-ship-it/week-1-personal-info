#personal information manager
#my first python project

#welcome message
print("Welcome to the Personal Information Manager!")
print("=" * 50)
print()

#store static information
name = "Bhargav"
age = 19
city = "Vizag"
hobby = "coding"

#display personal information
print("Personal Information:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Hobby: {hobby}")

favorite_food=""
while favorite_food =="":
    
    favorite_food = input("what is your favorite food? ")
favorite_color=""
while favorite_color == "":
    
    favorite_color = input("what is your favorite color? ")

print(f"Favorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")

#Calculate age in months
age_in_months = age * 12
print(f"Age in Months: {age_in_months}")

#goodbye message
print()
print("=" * 50)
print("Thank you for using the Personal Information Manager!")
