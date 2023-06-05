# Write a Python script to find the greatest number in a given list of numbers.
def find_greatest_number(numbers):
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest

# Example usage
num_list = [5, 10, 2, 8, 3]
greatest_num = find_greatest_number(num_list)
print("The greatest number is:", greatest_num)
