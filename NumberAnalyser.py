import math

def is_even(n): # this function checks if a number is even
    return n % 2 == 0 # the % is a modulus operator which returns the remainder of n divided by 2 and we are saying it has to be = to 0

def is_prime(n):
    if n <= 1: #prime numbers are greater than 1
        return False # if the number is less than or equal to 1, it is not prime
    
    for i in range(2, int(math.sqrt(n)) + 1): # this loops from 2 to the square root of n
        if n % i == 0: # if n is divisible by i, it is not prime
            return False
        return True # if no divisors were found, it is prime
    
def is_perfect_square(n):
    return int(math.sqrt(n)) ** 2 == n  # this converts the square root of n to an integer and squares it again to check if it equals n

def factorial(n):
        if n < 0:
            return "Undefined for negative numbers" #factorials can only be defined for positive numbers
        if n > 100:
            return "Too large to compute" #factorials grow very fast, so we limit it to 100
        return math.factorial(n) # Uses Python's built-in math.factorial() function to compute the factorial of n.

# Main CLI loop
def analyze_number():
    try:
        num = int(input("Enter a number: ")) #asks user to input a number
        print(f"\nAnalyzing {num}...")
        print("Even" if is_even(num) else "Odd")
        print("Prime" if is_prime(num) else "Not Prime")
        print("Perfect Square" if is_perfect_square(num) else "Not a Perfect Square")
        print(f"Factorial: {factorial(num)}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    analyze_number()
    
