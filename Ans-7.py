# Write a Python script to remove all non int values from a list.
def remove_non_integers(lst):
    return [x for x in lst if isinstance(x, int)]

# Example usage
mixed_list = [1, 'apple', 2.5, 3, 'banana', 4.7, 5]
integer_list = remove_non_integers(mixed_list)
print("List with non-integer values removed:", integer_list)
