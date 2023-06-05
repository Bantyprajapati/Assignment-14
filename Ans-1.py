# Write a Python script to create a list of first N natural numbers.
def generate_natural_numbers(n):
    natural_numbers = list(range(1, n + 1))
    return natural_numbers

# Example usage
N = 10  # Number of natural numbers
numbers = generate_natural_numbers(N)
print(numbers)
