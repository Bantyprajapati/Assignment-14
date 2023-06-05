# Write a Python script to create a list of first N odd natural numbers.
def generate_odd_numbers(n):
    odd_numbers = [2*i - 1 for i in range(1, n + 1)]
    return odd_numbers

# Example usage
N = 10  # Number of odd natural numbers
numbers = generate_odd_numbers(N)
print(numbers)
