# List to store the numbers
numbers = list()

# Get three numbers from the user
for i in range(3):
    numbers.append(int(input(f"Enter any number {i+1}: ")))
    
print("Your list is:", numbers)

# Determine the greatest number
if numbers[0] >= numbers[1] and numbers[0] >= numbers[2]:
    greatest = numbers[0]
elif numbers[1] >= numbers[0] and numbers[1] >= numbers[2]:
    greatest = numbers[1]
else:
    greatest = numbers[2]

print(f"The greatest number is: {greatest}")
