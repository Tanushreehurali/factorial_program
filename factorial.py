def factorial():
    n=int(input("Enter a number: "))

def display_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print("factorial:",fact)

if __name__ == "__main__":
    n = factorial()
    display_factorial(n)




