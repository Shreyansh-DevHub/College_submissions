def factorial(n):
    if n==0 or n ==1:
        return 1
    return n * factorial(n -1)

num1 = int(input("Enter a number to find its factorial: "))
print(f"factorial of the number {num1} = {factorial(num1)}")
print("name: shreyansh singh \nprn no.: 26013010907")