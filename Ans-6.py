# Write a Python script to calculate the sum of elements in a given list of numbers.
def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# Example usage
num_list = [5, 10, 2, 8, 3]
sum_of_elements = calculate_sum(num_list)
print("The sum of elements is:", sum_of_elements)
