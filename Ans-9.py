# Write a Python script to print indices of all occurrences of a given element in a given list.
def print_indices_of_element(lst, element):
    indices = [index for index, value in enumerate(lst) if value == element]
    if indices:
        print("Indices of element", element, ":", indices)
    else:
        print("Element", element, "not found in the list.")

# Example usage
my_list = [1, 2, 3, 2, 4, 5, 2]
given_element = 2
print("Indices of occurrences of element", given_element, ":")
print_indices_of_element(my_list, given_element)
