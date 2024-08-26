# Function to determine age category
def determine_age_category(age):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Invalid age"

# Get user input for age
try:
    age = int(input("Enter your age: "))

    # Determine and print the age category
    category = determine_age_category(age)
    print(f"You are a {category}.")

except ValueError:
    print("Invalid input. Please enter a valid number.")
