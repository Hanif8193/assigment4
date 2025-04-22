
C: int = 299792458

def main():
    mass_in_kg: float = float(input("Enter mass in kg: "))
    
    # Calculate energy using E = mc^2
    energy_in_joules: float = mass_in_kg * C ** 2
    print("m = " + str(mass_in_kg) + " kg")
    print("c = " + str(C) + " m/s")
    print("e = " + str(energy_in_joules) + " J")

if __name__ == "__main__":
    main()
