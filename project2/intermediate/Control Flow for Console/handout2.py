
# Mars Weight

"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():
   
   print("Welcome to the Mars Weight Calculator!") # Welcome message, prompts user for input and then calculates output based on provided inputs. Prints results
print("*****************************************")
earth_weight = float(input("Enter your weight on Earth (in pounds): "))
gravity_ratio = {
    "Marcury": 0.38,
    "Venus": 0.91,
    "Earth": 1.0,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 1.06,
    "Uranus": 0.92,
    "Neptune": 1.19,
     "Pluto": 0.59
 
 } # Dictionary of gravity ratios for different}
print("selected planet:")
for planet in gravity_ratio:
 print(f"- {planet}")

planet_choice = input("Enter the name of the planet: ").capitalize()
if planet_choice in gravity_ratio:
    new_weight = earth_weight * gravity_ratio[planet_choice]
    print(f"Your weight on {planet_choice} is: {new_weight:.2f} pounds")
else: 
    print("Invalid planet choice. Please try again.") 


if __name__ == "__main__":
    main()