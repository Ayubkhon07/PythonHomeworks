# 1. Write a Python script to sort (ascending and descending) a dictionary by value.
my_dict = {'apple': 10, 'banana': 2, 'cherry': 5}
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending Order:", sorted_dict_asc)
# 2. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
# Sample Dictionary
my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print("Updated Dictionary:", my_dict)
# 3. Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
new_dict = {}
for d in (dic1, dic2, dic3):
    new_dict.update(d)
print("Concatenated Dictionary:", new_dict)
# 4. Write a Python script to check whether a given key already exists in a dictionary.
my_dict = {0: 10, 1: 20}
key_to_check = 2

if key_to_check in my_dict:
    print(f"Key {key_to_check} exists in the dictionary.")
else:
    print(f"Key {key_to_check} does not exist in the dictionary.")
# 5. Write a Python program to iterate over dictionaries using for loops.
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
n = 5
squared_dict = {}

for x in range(1, n + 1):
    squared_dict[x] = x * x

print("Squared Dictionary:", squared_dict)
# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
squared_dict = {x: x * x for x in range(1, 16)}
print("Squared Dictionary:", squared_dict)
# 8. Write a Python script to merge two Python dictionaries.
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print("Merged Dictionary:", merged_dict)
# 9. Write a Python program to iterate over dictionaries using for loops.
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
# 10. Write a Python program to sum all the items in a dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
total_sum = sum(my_dict.values())
print("Sum of all items in the dictionary:", total_sum)
# 11. Write a Python program to multiply all the items in a dictionary.  
my_dict = {'a': 1, 'b': 2, 'c': 3}
result = 1
for value in my_dict.values():
    result *= value
print("Product of all items:", result)
# 12. Write a Python program to remove a key from a dictionary.  
my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = 'b'
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
print("Updated Dictionary:", my_dict)
# 13. Write a Python program to map two lists into a dictionary.  
keys = ['a', 'b', 'c']
values = [1, 2, 3]
mapped_dict = dict(zip(keys, values))
print("Mapped Dictionary:", mapped_dict)
# 14. Write a Python program to sort a given dictionary by key.  
my_dict = {'b': 1, 'c': 2, 'a': 3}
sorted_dict = dict(sorted(my_dict.items()))
print("Sorted Dictionary by Key:", sorted_dict)
# 15. Write a Python program to get the maximum and minimum values of a dictionary.
my_dict = {'a': 10, 'b': 20, 'c': 5}
max_value = max(my_dict.values())
min_value = min(my_dict.values())
print("Max Value:", max_value)
print("Min Value:", min_value)
# 16. Write a Python program to get a dictionary from an object's fields.  
class MyClass:
    def __init__(self):
        self.field1 = 1
        self.field2 = 2
        self.field3 = 3

obj = MyClass()
obj_dict = obj.__dict__
print("Object's Field Dictionary:", obj_dict)
# 17. Write a Python program to remove duplicates from the dictionary.  
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}
unique_dict = {}
for key, value in my_dict.items():
    if value not in unique_dict.values():
        unique_dict[key] = value
print("Dictionary with Duplicates Removed:", unique_dict)
# 18. Write a Python program to check if a dictionary is empty or not.  
my_dict = {}
if not my_dict:
    print("The dictionary is empty.")
else:
    print("The dictionary is not empty.")
# 19. Write a Python program to combine two dictionary by adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})  
from collections import Counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
combined_dict = Counter(d1) + Counter(d2)
print("Combined Dictionary:", combined_dict)
# 20. Write a Python program to print all distinct values in a dictionary.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}  
sample_data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
unique_values = {v for d in sample_data for v in d.values()}
print("Unique Values:", unique_values)
# 21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd
from itertools import product

data = {'1': ['a', 'b'], '2': ['c', 'd']}
combinations = [''.join(x) for x in product(*data.values())]
print("Combinations:")
for combination in combinations:
    print(combination)
# 22. Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
highest_3 = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True)[:3])
print("Highest 3 Values:", highest_3)
# 23. Write a Python program to combine values in a list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})
from collections import Counter

data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
combined_data = Counter()
for d in data:
    combined_data[d['item']] += d['amount']
print("Combined Values:", combined_data)
# 24. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
from collections import Counter

sample_string = 'w3resource'
count_dict = dict(Counter(sample_string))
print("Letter Count Dictionary:", count_dict)
# 25. Write a Python program to print a dictionary in table format.
my_dict = {'a': 1, 'b': 2, 'c': 3}

print(f"{'Key':<10} {'Value':<10}")

for key, value in my_dict.items():
    print(f"{key:<10} {value:<10}")
# 26. Write a Python program to count the values associated with a key in a dictionary.
# Expected Output:
# 6
# 2  
sample_data = {'1': [1, 2, 3], '2': [1, 2], '3': [1, 2, 3, 4, 5, 6]}
count_dict = {k: len(v) for k, v in sample_data.items()}
print("Count of Values Associated with Keys:", count_dict)
# 27. Write a Python program to convert a list into a nested dictionary of keys.
my_list = [1, 2, 3, 4]
nested_dict = current = {}
for item in my_list:
    current[item] = {}
    current = current[item]
print("Nested Dictionary:", nested_dict)
# 28. Write a Python program to sort a list alphabetically in a dictionary.
my_dict = {'fruits': ['apple', 'banana', 'cherry', 'date']}
my_dict['fruits'].sort()
print("Sorted Dictionary:", my_dict)
# 29. Write a Python program to remove spaces from dictionary keys.
my_dict = {'key 1': 1, 'key 2': 2, 'key 3': 3}
new_dict = {key.replace(' ', ''): value for key, value in my_dict.items()}
print("Dictionary with Spaces Removed from Keys:", new_dict)
# 30. Write a Python program to get the top three items in a shop.
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3  
shop_items = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
top_three = dict(sorted(shop_items.items(), key=lambda item: item[1], reverse=True)[:3])
print("Top Three Items:")
for item, price in top_three.items():
    print(item, price)
# 31. Write a Python program to get the key, value and item in a dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}, Item: ({key}, {value})")
# 32. Write a Python program to print a dictionary line by line.
# my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print(f"{key}: {value}")  
# 33. Write a Python program to check if multiple keys exist in a dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys_to_check = ['a', 'c']

if all(key in my_dict for key in keys_to_check):
    print("All keys exist in the dictionary.")
else:
    print("Not all keys exist in the dictionary.")
# 34. Write a Python program to count the number of items in a dictionary value that is a list.
my_dict = {'a': [1, 2, 3], 'b': [4, 5], 'c': [6, 7, 8, 9]}

count_dict = {key: len(value) for key, value in my_dict.items()}
print("Count of items in dictionary values:", count_dict)
# 35. Write a Python program to sort Counter by value.
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
from collections import Counter

sample_data = {'Math': 81, 'Physics': 83, 'Chemistry': 87}
sorted_data = sorted(sample_data.items(), key=lambda item: item[1], reverse=True)
print("Sorted Data by Value:", sorted_data)
# 36. Write a Python program to create a dictionary from two lists without losing duplicate values.
# Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# Expected Output: defaultdict(<class 'set'>, {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}})
from collections import defaultdict

keys = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
values = [1, 2, 2, 3]
dict_with_duplicates = defaultdict(set)

for key, value in zip(keys, values):
    dict_with_duplicates[key].add(value)

print("Dictionary with Duplicates:", dict_with_duplicates)
# 37. Write a Python program to replace dictionary values with their sums.
my_dict = {'a': [1, 2, 3], 'b': [4, 5], 'c': [6, 7, 8, 9]}

sum_dict = {key: sum(value) for key, value in my_dict.items()}
print("Dictionary with Sums:", sum_dict)
# 38. Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y
dict1 = {'key1': 1, 'key2': 3, 'key3': 2}
dict2 = {'key1': 1, 'key2': 2}

matched_keys = {k: v for k, v in dict1.items() if k in dict2 and dict1[k] == dict2[k]}
for key, value in matched_keys.items():
    print(f"{key}: {value} is present in both dictionaries.")
# 39. Write a Python program to store dictionary data in a JSON file.
# Original dictionary:
# {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}
# <class 'dict'>
# Json file to dictionary:
# {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}  
import json

# Original dictionary
data = {
    'students': [
        {'firstName': 'Nikki', 'lastName': 'Roysden'},
        {'firstName': 'Mervin', 'lastName': 'Friedland'},
        {'firstName': 'Aron', 'lastName': 'Wilkins'}
    ],
    'teachers': [
        {'firstName': 'Amberly', 'lastName': 'Calico'},
        {'firstName': 'Regine', 'lastName': 'Agtarap'}
    ]
}

# Write to JSON file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

# Read from JSON file
with open('data.json', 'r') as json_file:
    loaded_data = json.load(json_file)

print("Loaded Data:", loaded_data)
# 40. Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.
# {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# 15
# 25
# 35
# x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
# y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
# z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]
my_dict = {
    'x': list(range(11, 20)),
    'y': list(range(21, 30)),
    'z': list(range(31, 40))
}

print("Fifth value of key 'x':", my_dict['x'][4])
print("Fifth value of key 'y':", my_dict['y'][4])
print("Fifth value of key 'z':", my_dict['z'][4])

print("x has value", my_dict['x'])
print("y has value", my_dict['y'])
print("z has value", my_dict['z'])
# 41. Write a Python program to drop empty items from a given dictionary.
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}
original_dict = {'c1': 'Red', 'c2': 'Green', 'c3': None}
new_dict = {k: v for k, v in original_dict.items() if v is not None}
print("New Dictionary after dropping empty items:", new_dict)
# 42. Write a Python program to filter a dictionary based on values.
# Original Dictionary:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
original_dict = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
filtered_dict = {k: v for k, v in original_dict.items() if v > 170}
print("Marks greater than 170:", filtered_dict)
# 43. Write a Python program to convert more than one list to a nested dictionary.
# Original strings:
# ['S001', 'S002', 'S003', 'S004']
# ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# [85, 98, 89, 92]
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
ids = ['S001', 'S002', 'S003', 'S004']
names = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
scores = [85, 98, 89, 92]

nested_dict = [{id_: {name: score}} for id_, name, score in zip(ids, names, scores)]
print("Nested dictionary:", nested_dict)
# 44. Write a Python program to filter the height and width of students, which are stored in a dictionary.
# Original Dictionary:
# {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# Height > 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}
students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
filtered_students = {k: v for k, v in students.items() if v[0] > 6 and v[1] > 70}
print("Height > 6ft and Weight > 70kg:", filtered_students)
# 45. Write a Python program to verify that all values in a dictionary are the same.
# Original Dictionary:
# {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# Check all are 12 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False
original_dict = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
all_equal_12 = all(value == 12 for value in original_dict.values())
all_equal_10 = all(value == 10 for value in original_dict.values())

print("Check all are 12 in the dictionary:", all_equal_12)
print("Check all are 10 in the dictionary:", all_equal_10)
# 46. Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.
# Original list:
# [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
original_list = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
grouped_dict = {}

for k, v in original_list:
    grouped_dict.setdefault(k, []).append(v)

print("Grouped dictionary:", grouped_dict)
# 47. Write a Python program to split a given dictionary of lists into lists of dictionaries.
# Original dictionary of lists:
# {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# Split said dictionary of lists into list of dictionaries:
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
original_dict = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
split_list = [dict(zip(original_dict.keys(), values)) for values in zip(*original_dict.values())]
print("Split list of dictionaries:", split_list)
# 48. Write a Python program to remove a specified dictionary from a given list.
# Original list of dictionary:
# [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# Remove id #FF0000 from the said list of dictionary:
# [{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
original_list = [
    {'id': '#FF0000', 'color': 'Red'},
    {'id': '#800000', 'color': 'Maroon'},
    {'id': '#FFFF00', 'color': 'Yellow'},
    {'id': '#808000', 'color': 'Olive'}
]
id_to_remove = '#FF0000'
updated_list = [d for d in original_list if d.get('id') != id_to_remove]
print("Updated list:", updated_list)
# 49. Write a Python program to convert string values of a given dictionary into integer/float datatypes.
# Original list:
# [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# String values of a given dictionary, into integer types:
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
# Original list:
# [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
# String values of a given dictionary, into float types:
# [{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]
original_list = [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
converted_list_int = [{k: int(v) for k, v in d.items()} for d in original_list]
print("Converted to integers:", converted_list_int)

original_list = [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
converted_list_float = [{k: float(v) for k, v in d.items()} for d in original_list]
print("Converted to floats:", converted_list_float)
# 50. A Python dictionary contains List as a value. Write a Python program to clear the list values in the said dictionary.
# Original Dictionary:
# {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# Clear the list values in the said dictionary:
# {'C1': [], 'C2': [], 'C3': []}
original_dict = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
cleared_dict = {k: [] for k in original_dict}
print("Clear the list values in the said dictionary:", cleared_dict)
# 51. A Python Dictionary contains List as a value. Write a Python program to update the list values in the said dictionary.
# Original Dictionary:
# {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
# Update the list values of the said dictionary:
# {'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}
original_dict = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
updated_dict = {k: [value + 1 for value in v] for k, v in original_dict.items()}
print("Update the list values in the said dictionary:", updated_dict)
# 52. Write a Python program to extract a list of values from a given list of dictionaries.
# Original Dictionary:
# [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# Extract a list of values from said list of dictionaries where subject = Science
# [92, 94, 88]
# Original Dictionary:
# [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# Extract a list of values from said list of dictionaries where subject = Math
# [90, 89, 92]
dict_list = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
subject = 'Science'
extracted_values = [d[subject] for d in dict_list if subject in d]
print("Extract a list of values where subject =", subject, extracted_values)
# 53. Write a Python program to find the length of a dictionary of values.
my_dict = {'a': [1, 2, 3], 'b': [4, 5], 'c': [6, 7, 8, 9]}
length_dict = {k: len(v) for k, v in my_dict.items()}
print("Length of dictionary values:", length_dict)
# 54. Write a Python program to get the depth of a dictionary.
def get_depth(d, level=1):
    if not isinstance(d, dict) or not d:
        return level
    return max(get_depth(v, level + 1) for v in d.values())

my_dict = {'a': 1, 'b': {'c': {'d': {}}}}
depth = get_depth(my_dict)
print("Depth of the dictionary:", depth)
# 55. Write a Python program to access dictionary key's element by index.
# Expected Output:
# physics
# math
# chemistry
my_dict = {'physics': 1, 'math': 2, 'chemistry': 3}
keys_list = list(my_dict.keys())
print(keys_list[0])  # physics
print(keys_list[1])  # math
print(keys_list[2])  # chemistry
# 56. Write a Python program to convert a dictionary into a list of lists.
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Convert the said dictionary into a list of lists:
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Convert the said dictionary into a list of lists:
# [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]
original_dict = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
list_of_lists = [[k, v] for k, v in original_dict.items()]
print("Convert the dictionary into a list of lists:", list_of_lists)
# 57. Write a Python program to filter even numbers from a dictionary of values.
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# Filter even numbers from said dictionary values:
# {'V': [], 'VI': [], 'VII': [2]}
original_dict = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
filtered_dict = {k: [num for num in v if num % 2 == 0] for k, v in original_dict.items()}
print("Filter even numbers from the dictionary values:", filtered_dict)
# 58. Write a Python program to get all combinations of key-value pairs in a given dictionary.
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Combinations of key-value pairs of the said dictionary:
# [{'V': [1, 4, 6, 10], 'VI': [1, 4, 12]}, {'V': [1, 4, 6, 10], 'VII': [1, 3, 8]}, {'VI': [1, 4, 12], 'VII': [1, 3, 8]}]
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5]}
# Combinations of key-value pairs of the said dictionary:
# [{'V': [1, 3, 5], 'VI': [1, 5]}]
from itertools import combinations

original_dict = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
keys = original_dict.keys()
comb_dicts = [dict(comb) for i in range(1, len(keys) + 1) for comb in combinations(original_dict.items(), i)]
print("Combinations of key-value pairs of the dictionary:", comb_dicts)
# 59. Write a Python program to find the specified number of maximum values in a given dictionary.
# Original Dictionary:
# {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# 1 maximum value(s) in the said dictionary:
# ['f']
# 2 maximum value(s) in the said dictionary:
# ['f', 'i']
# 5 maximum value(s) in the said dictionary:
# ['f', 'i', 'g', 'd', 'c']
original_dict = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
max_n = 5
max_values = sorted(original_dict, key=original_dict.get, reverse=True)[:max_n]
print(max_n, "maximum value(s) in the said dictionary:", max_values)
# 60. Write a Python program to find the shortest list of values for the keys in a given dictionary.
# Original Dictionary: {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]} Shortest list of values with the keys of the said dictionary: ['VI', 'VIII', 'X']  
original_dict = {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}
shortest_lists = [k for k, v in original_dict.items() if len(v) == min(map(len, original_dict.values()))]
print("Shortest list of values with the keys of the dictionary:", shortest_lists)
# 61. Write a Python program to count the frequency of a dictionary.
# Original Dictionary:
# {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
# Count the frequency of the said dictionary:
# Counter({10: 2, 40: 2, 20: 2, 70: 1, 80: 1})
from collections import Counter

original_dict = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
frequency = Counter(original_dict.values())
print("Count the frequency of the said dictionary:", frequency)
# 62. Write a Python program to extract values from a given dictionary and create a list of lists from those values.
# Original Dictionary:
# [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
# Extract values from the said dictionarie and create a list of lists using those values:
# [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# [[1, 'Jean Castro'], [2, 'Lula Powell'], [3, 'Brian Howell'], [4, 'Lynne Foster'], [5, 'Zachary Simon']]
# [['Jean Castro', 'V'], ['Lula Powell', 'V'], ['Brian Howell', 'VI'], ['Lynne Foster', 'VI'], ['Zachary Simon', 'VII']]
dict_list = [
    {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'},
    {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
    {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
    {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
    {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
]

list_of_lists = [[d['student_id'], d['name'], d['class']] for d in dict_list]
list_of_id_name = [[d['student_id'], d['name']] for d in dict_list]
list_of_name_class = [[d['name'], d['class']] for d in dict_list]

print("List of lists:", list_of_lists)
print("List of ID and Name:", list_of_id_name)
print("List of Name and Class:", list_of_name_class)
# 63. Write a Python program to convert a given list of lists to a dictionary.
# Original list of lists:
# [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# Convert the said list of lists to a dictionary:
# {1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}
list_of_lists = [
    [1, 'Jean Castro', 'V'],
    [2, 'Lula Powell', 'V'],
    [3, 'Brian Howell', 'VI'],
    [4, 'Lynne Foster', 'VI'],
    [5, 'Zachary Simon', 'VII']
]

converted_dict = {item[0]: item[1:] for item in list_of_lists}
print("Converted dictionary:", converted_dict)
# 64. Write a Python program that creates key-value list pairings within a dictionary.
# Original dictionary:
# {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# A key-value list pairings of the said dictionary:
# [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]
original_dict = {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
pairings = [{k: v[0] for k, v in original_dict.items()}]
print("Key-value list pairings:", pairings)
# 65. Write a Python program to get the total length of all values in a given dictionary with string values.
# Original dictionary:
# {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
# Total length of all values of the said dictionary with string values:
# 20
original_dict = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
total_length = sum(len(value) for value in original_dict.values())
print("Total length of all values:", total_length)
# 66. Write a Python program to check if a specific key and a value exist in a dictionary.
# Original dictionary:
# [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
# Check if a specific Key and a value exist in the said dictionary:
# True
# True
# True
# False
# False
# False  
dict_list = [
    {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'},
    {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
    {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
    {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
    {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
]

key_to_check = 'student_id'
value_to_check = 3

exist = any(d.get(key_to_check) == value_to_check for d in dict_list)
print("Does the key-value pair exist?", exist)
# 67. Write a Python program to invert a given dictionary with non-unique hashable values.
# Sample Output:
# {8: ['Ora Mckinney', 'Mathew Gilbert'], 7: ['Theodore Hollandl', 'Mae Fleming', 'Ivan Little']}
dict_list = [
    {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'},
    {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
    {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
    {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
    {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
]

key_to_check = 'student_id'
value_to_check = 3

exist = any(d.get(key_to_check) == value_to_check for d in dict_list)
print("Does the key-value pair exist?", exist)
# 68. Write a Python program to combine two or more dictionaries, creating a list of values for each key.
# Sample Output:
# Original dictionaries:
# {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
# {'x': 300, 'y': 'Red', 'z': 600}
# Combined dictionaries, creating a list of values for each key:
# {'w': [50], 'x': [100, 300], 'y': ['Green', 'Red'], 'z': [400, 600]}
dict1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
dict2 = {'x': 300, 'y': 'Red', 'z': 600}

combined_dict = {}
for d in (dict1, dict2):
    for k, v in d.items():
        combined_dict.setdefault(k, []).append(v)

print("Combined dictionaries:", combined_dict)
# 69. Write a Python program to group the elements of a given list based on the given function.
# Sample Output:
# Original list & function:
# [7, 23, 3.2, 3.3, 8.4] Function name: floor:
# Group the elements of the said list based on the given function:
# {7: [7], 23: [23], 3: [3.2, 3.3], 8: [8.4]}
# Original list & function:
# ['Red', 'Green', 'Black', 'White', 'Pink'] Function name: len:
# Group the elements of the said list based on the given function:
# {3: ['Red'], 5: ['Green', 'Black', 'White'], 4: ['Pink']}
from math import floor

original_list1 = [7, 23, 3.2, 3.3, 8.4]
grouped_by_floor = {}
for item in original_list1:
    key = floor(item)
    grouped_by_floor.setdefault(key, []).append(item)
print("Group by floor:", grouped_by_floor)

original_list2 = ['Red', 'Green', 'Black', 'White', 'Pink']
grouped_by_len = {}
for item in original_list2:
    key = len(item)
    grouped_by_len.setdefault(key, []).append(item)
print("Group by length:", grouped_by_len)
# 70. Write a Python program to map the values of a given list to a dictionary using a function, where the key-value pairs consist of the original value as the key and the result of the function as the value.
# Sample Output:
# {1: 1, 2: 4, 3: 9, 4: 16}
def square(x):
    return x * x

original_list = [1, 2, 3, 4]
mapped_dict = {x: square(x) for x in original_list}
print("Mapped dictionary:", mapped_dict)
# 71. Write a Python program to retrieve the value of the nested key indicated by the given selector list from a dictionary or list.
# Sample Output:
# Russell
# 2
def get_nested_value(data, selector):
    for key in selector:
        data = data[key]
    return data

sample_dict = {'key1': {'key2': {'key3': 'Russell'}}}
selector_list = ['key1', 'key2', 'key3']
print(get_nested_value(sample_dict, selector_list))  # Output: Russell

sample_list = [{'a': 1}, {'b': 2}]
selector_list = [1, 'b']
print(get_nested_value(sample_list, selector_list))  # Output: 2
# 72. Write a Python program to invert a dictionary with unique hashable values.
# Sample Output:
# {10: 'Theodore', 11: 'Mathew', 9: 'Roxanne'}
original_dict = {'Theodore': 10, 'Mathew': 11, 'Roxanne': 9}
inverted_dict = {v: k for k, v in original_dict.items()}
print("Inverted dictionary:", inverted_dict)
# 73. Write a Python program to convert a list of dictionaries into a list of values corresponding to the specified key.
# Sample Output:
# Original list of dictionaries:
# [{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]
# Convert a list of dictionaries into a list of values corresponding to the specified key:
# [18, 22, 20, 18]
dict_list = [
    {'name': 'Theodore', 'age': 18},
    {'name': 'Mathew', 'age': 22},
    {'name': 'Roxanne', 'age': 20},
    {'name': 'David', 'age': 18}
]
key = 'age'
values_list = [d[key] for d in dict_list]
print("List of values corresponding to the specified key:", values_list)
# 74. Write a Python program to create a dictionary with the same keys as the given dictionary and values generated by running the given function for each value.
# Sample Output:
# Original dictionary elements:
# {'Theodore': {'user': 'Theodore', 'age': 45}, 'Roxanne': {'user': 'Roxanne', 'age': 15}, 'Mathew': {'user': 'Mathew', 'age': 21}}
# Dictionary with the same keys:
# {'Theodore': 45, 'Roxanne': 15, 'Mathew': 21}
original_dict = {
    'Theodore': {'user': 'Theodore', 'age': 45},
    'Roxanne': {'user': 'Roxanne', 'age': 15},
    'Mathew': {'user': 'Mathew', 'age': 21}
}

new_dict = {k: v['age'] for k, v in original_dict.items()}
print("Dictionary with the same keys:", new_dict)
# 75. Write a Python program to find all keys in a dictionary that have the given value.
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# Find all keys in the said dictionary that have the specified value:
# ['Roxanne', 'Betty']
original_dict = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
value_to_find = 20
keys_with_value = [k for k, v in original_dict.items() if v == value_to_find]
print("Keys with the specified value:", keys_with_value)
# 76. Write a Python program to combine two lists into a dictionary. The elements of the first one serve as keys and the elements of the second one serve as values. Each item in the first list must be unique and hashable.
# Sample Output:
# Original lists:
# ['a', 'b', 'c', 'd', 'e', 'f']
# [1, 2, 3, 4, 5]
# Combine the values of the said two lists into a dictionary:
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
keys_list = ['a', 'b', 'c', 'd', 'e', 'f']
values_list = [1, 2, 3, 4, 5]
combined_dict = dict(zip(keys_list, values_list))
print("Combined dictionary:", combined_dict)
# 77. Write a Python program to transform a dictionary into a list of tuples.
# Sample Output:
# Original Dictionary:
# {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# Convert the said dictionary to a list of tuples:
# [('Red', 1), ('Green', 3), ('White', 5), ('Black', 2), ('Pink', 4)]
original_dict = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
list_of_tuples = list(original_dict.items())
print("List of tuples:", list_of_tuples)
# 78. Write a Python program to create a flat list of all the keys in a flat dictionary.
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# Create a flat list of all the keys of the said flat dictionary:
# ['Theodore', 'Roxanne', 'Mathew', 'Betty']
original_dict = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
keys_list = list(original_dict.keys())
print("Flat list of all keys:", keys_list)
# 79. Write a Python program to create a flat list of all the values in a flat dictionary.
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# Create a flat list of all the values of the said flat dictionary:
# [19, 20, 21, 20]
original_dict = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
values_list = list(original_dict.values())
print("Flat list of all values:", values_list)
# 80. Write a Python program to find the key of the maximum value in a dictionary.
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# Finds the key of the maximum and minimum value of the said dictionary:
# ('Roxanne', 'Theodore')
original_dict = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
max_key = max(original_dict, key=original_dict.get)
min_key = min(original_dict, key=original_dict.get)
print("Key of the maximum value:", max_key)
print("Key of the minimum value:", min_key)