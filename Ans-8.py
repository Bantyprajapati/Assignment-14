# Write a Python script to print distinct elements along with their frequencies of occurrence in the list.
def print_element_frequencies(lst):
    element_freq = {}
    for element in lst:
        if element in element_freq:
            element_freq[element] += 1
        else:
            element_freq[element] = 1
    
    for element, frequency in element_freq.items():
        print("Element:", element, "Frequency:", frequency)

# Example usage
my_list = [1, 2, 1, 3, 4, 2, 5, 3, 2, 4, 1, 5, 5]
print("Distinct elements and their frequencies:")
print_element_frequencies(my_list)
