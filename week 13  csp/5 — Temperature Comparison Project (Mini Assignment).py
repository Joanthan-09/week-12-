# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:


temperature = float(input("Enter today's temperature: "))

if temperature < -10 or temperature > 110:
        print("Extreme temperature warning!")
elif temperature < 40:
        print("It's cold.")
elif temperature >= 40 and temperature < 75:
        print("It's warm.")
else:  # temperature >= 75
        print("It's hot.")
