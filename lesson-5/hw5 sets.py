# 1. Write a Python program to create a set.
my_set = {1, 2, 3, 4, 5}
print(my_set)
# 2. Write a Python program to iterate over sets.
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)
# 3. Write a Python program to add member(s) to a set.
my_set = {1, 2, 3}
my_set.add(4)
my_set.update([5, 6])
print(my_set)
# 4. Write a Python program to remove item(s) from a given set.
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)  # Raises KeyError if 3 is not in the set
my_set.discard(4)  # Does not raise an error if 4 is not in the set
print(my_set)
# 5. Write a Python program to remove an item from a set if it is present in the set.
my_set = {1, 2, 3, 4, 5}
if 3 in my_set:
    my_set.remove(3)
print(my_set)
# 6. Write a Python program to create an intersection of sets.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersection_set = set1 & set2
print(intersection_set)
# 7. Write a Python program to create a union of sets.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
union_set = set1 | set2
print(union_set)
# 8. Write a Python program to create set difference.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
difference_set = set1 - set2
print(difference_set)
# 9. Write a Python program to create a symmetric difference.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
sym_difference_set = set1 ^ set2
print(sym_difference_set)
# 10. Write a Python program to check if a set is a subset of another set.
set1 = {1, 2, 3}
set2 = {1, 2}
print(set2.issubset(set1))
# 11. Write a Python program to create a shallow copy of sets.
# Note : Shallow copy is a bit-wise copy of an object. A new object is created that has an exact copy of the values in the original object.
set1 = {1, 2, 3}
set_copy = set1.copy()
print(set_copy)
# 12. Write a Python program to remove all elements from a given set.
my_set = {1, 2, 3, 4, 5}
my_set.clear()
print(my_set)
# 13. Write a Python program that uses frozensets.
# Note: Frozensets behave just like sets except they are immutable.
frozen_set = frozenset([1, 2, 3, 4])
print(frozen_set)
# 14. Write a Python program to find the maximum and minimum values in a set.
my_set = {1, 2, 3, 4, 5}
print(max(my_set))
print(min(my_set))
# 15. Write a Python program to find the length of a set.
my_set = {1, 2, 3, 4, 5}
print(len(my_set))
# 16. Write a Python program to check if a given value is present in a set or not.
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)
# 17. Write a Python program to check if two given sets have no elements in common.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))
# 18. Write a Python program to check if a given set is a superset of itself and a superset of another given set.
set1 = {1, 2, 3}
set2 = {1, 2}
print(set1.issuperset(set2))
# 19. Write a Python program to find elements in a given set that are not in another set.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
difference_set = set1.difference(set2)
print(difference_set)
# 20. Write a Python program to remove the intersection of a second set with a first set.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.difference_update(set2)
print(set1)
# 21. Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
unique_words = set(words)
word_count = {word: words.count(word) for word in unique_words}
print(word_count)
# 22. Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.
def find_pairs(lst, target_sum):
    pairs = []
    seen = set()
    for number in lst:
        if target_sum - number in seen:
            pairs.append((number, target_sum - number))
        seen.add(number)
    return pairs

numbers = [1, 2, 3, 4, 5, 6]
target = 7
print(find_pairs(numbers, target))
# 23. Write a Python program to find the longest common prefix of all strings. Use the Python set.
def longest_common_prefix(strings):
    if not strings:
        return ""
    prefix = strings[0]
    for string in strings[1:]:
        while string.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

strings = ["flower", "flow", "flight"]
print(longest_common_prefix(strings))
# 24. Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set.
def max_product_pair(numbers):
    max1 = max2 = float('-inf')
    for num in numbers:
        if num > max1:
            max1, max2 = num, max1
        elif num > max2:
            max2 = num
    return max1, max2

numbers = [1, 20, 3, 4, 5]
print(max_product_pair(numbers))
# 25. Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
missing_in_set2 = set1 - set2
missing_in_set1 = set2 - set1
print("Missing in set2:", missing_in_set2)
print("Missing in set1:", missing_in_set1)
# 26. Write a Python program to find all the anagrams and group them together from a given list of strings. Use the Python data type.
from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    return list(anagrams.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
# 27. Write a Python program to find all the anagrams in a given list of strings and then group them together. Use the Python data type.
def three_sum(nums, target):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == target:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
    return result

numbers = [1, 2, -2, -1, 0, 3, -3]
target = 0
print(three_sum(numbers, target))
# 28. Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.
def third_largest(numbers):
    unique_numbers = sorted(set(numbers), reverse=True)
    return unique_numbers[2] if len(unique_numbers) >= 3 else None

numbers = [10, 4, 5, 8, 1, 9, 7, 6]
print(third_largest(numbers))
# 29. Write a Python program to find the third largest number from a given list of numbers.Use the Python set data type.
def third_largest(numbers):
    unique_numbers = sorted(set(numbers), reverse=True)
    return unique_numbers[2] if len(unique_numbers) >= 3 else None

numbers = [10, 4, 5, 8, 1, 9, 7, 6]
print(third_largest(numbers))
# 30. Write a Python program to remove all duplicates from a given list of strings and return a list of unique strings. Use the Python set data type.
def unique_strings(strings):
    return list(set(strings))

strings = ["apple", "banana", "apple", "orange", "banana", "kiwi"]
print(unique_strings(strings))