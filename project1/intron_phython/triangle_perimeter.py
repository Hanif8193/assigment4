def main():

    side1 = float(input("Enter the length of the first side of the triangle: "))
    side2 = float(input("Enter the length of the second side of the triangle: "))
    side3 = float(input("Enter the length of the third side of the triangle: "))

    perameter = side1 + side2 + side3
    print(f"\033[1;3m The perimeter of the triangle is: {perameter} \033[0m")

    
if __name__ == "__main__":
    main()
