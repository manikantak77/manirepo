# Ask for the user's name
name = input("Enter your name: ")

# Ask for the user's birth year and calculate age
birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year

# Output formatted string
print(f"Hello, {name}! You are turning {age} years old this year.")
