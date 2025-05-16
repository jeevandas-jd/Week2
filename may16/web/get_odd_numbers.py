# filename: get_odd_numbers.py
def get_odd_numbers(numbers):
    """
    This function takes a list of integers and returns a new list containing only the odd numbers.
    """
    odd_numbers = [number for number in numbers if number % 2 != 0]
    return odd_numbers

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = get_odd_numbers(numbers)
print(f"The odd numbers in the list are: {odd_numbers}")

numbers2 = [-1, 0, 1, 2, -3]
odd_numbers2 = get_odd_numbers(numbers2)
print(f"The odd numbers in the list are: {odd_numbers2}")

numbers3 = [2,4,6,8,10]
odd_numbers3 = get_odd_numbers(numbers3)
print(f"The odd numbers in the list are: {odd_numbers3}")
