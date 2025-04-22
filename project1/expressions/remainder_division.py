def main():

     dividend: int = int(input("Enter the dividend: "))
     divisor: int = int(input("Enter the divisor: "))

     quotient: int = dividend // divisor
     remainder: int = dividend % divisor

     print("the result of the division is: " + str(quotient)+ "with a reminder  of: " +str(remainder))
 
if __name__ == "__main__":
     main()