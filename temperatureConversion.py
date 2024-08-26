# celsius convertion to fahrenheit
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to determine the temperature category
def determine_temperature_category(fahrenheit):
    if fahrenheit >= 86:
        return "Hot"
    elif 68 <= fahrenheit < 86:
        return "Moderate"
    else:
        return "Cold"

# Get user input for temperature in Celsius
try:
    celsius = float(input("Enter the temperature in Celsius: "))

    # Convert Celsius to Fahrenheit
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}°F")

    # Determine and print the temperature category
    category = determine_temperature_category(fahrenheit)
    print(f"The weather is {category}.")

except ValueError:
    print("Invalid input. Please enter a valid number.")
