# Write a Python script to find the smallest number in a given list of numbers.
def find_smallest_number(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

# Example usage
num_list = [5, 10, 2, 8, 3]
smallest_num = find_smallest_number(num_list)
print("The smallest number is:", smallest_num)
