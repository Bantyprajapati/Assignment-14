# Write a Python script to create a list of first N even natural numbers.
def generate_even_numbers(n):
    even_numbers = [2*i for i in range(1, n + 1)]
    return even_numbers

# Example usage
N = 10  # Number of even natural numbers
numbers = generate_even_numbers(N)
print(numbers)
