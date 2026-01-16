def get_number():
    return int(input("Enter a number: "))

def display_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(f"\nFactorial of {n} is {fact}")

if __name__ == "__main__":
    n = get_number()
    display_factorial(n)









