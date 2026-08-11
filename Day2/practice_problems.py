
numbers = [12, 45, 2, 99, 23, 67, 8]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(f"1. Largest number: {largest}\n")


numbers_for_second = [12, 45, 2, 99, 23, 67, 8]
first = float('-inf')
second = float('-inf')

for num in numbers_for_second:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print(f"2. List: {numbers_for_second}")
print(f"   Second largest number: {second}\n")


numbers_with_duplicates = [1, 3, 5, 3, 7, 1, 9, 5, 2]
unique_list = set(numbers_with_duplicates)
print(f"3. Original list with duplicates: {numbers_with_duplicates}")
print(f"   List after removing duplicates: {unique_list}\n")


sample_list = [10, 20, 30, 40, 50]
reversed_list = []
for i in range(len(sample_list) - 1, -1, -1):
    reversed_list.append(sample_list[i])
print(f"4. Original list: {sample_list}")
print(f"   Reversed list: {reversed_list}\n")


list_a = [1, 2, 3, 4, 5, 6]
list_b = [4, 5, 6, 7, 8, 9]
common_elements = []
for element in list_a:
    if element in list_b and element not in common_elements:
        common_elements.append(element)
print(f"5. List A: {list_a}")
print(f"   List B: {list_b}")
print(f"   Common elements: {common_elements}\n")




fruits_tuple = ("apple", "banana", "apple", "cherry", "apple", "mango")
target_fruit = "apple"
count = 0
for fruit in fruits_tuple:
    if fruit == target_fruit:
        count += 1
print(f"1. Fruits tuple: {fruits_tuple}")
print(f"   Occurrences of '{target_fruit}': {count}\n")


original_tuple = (10, 20, 30, 40)
converted_list = list(original_tuple)
 
new_tuple = tuple(converted_list)
print(f"2. Original Tuple: {original_tuple}")
print(f"   Converted to List {converted_list}")
print(f"   Converted back to Tuple: {new_tuple}\n")





raw_data = ["python", "java", "c++", "python", "javascript", "java"]
unique_set = set(raw_data)
print(f"1. Raw data list: {raw_data}")
print(f"   Unique values (Set): {unique_set}\n")


set_x = {1, 2, 3, 4, 5}
set_y = {4, 5, 6, 7, 8}

union_result = set_x.union(set_y)
intersection_result = set_x.intersection(set_y)

print(f"2. Set X: {set_x}")
print(f"   Set Y: {set_y}")
print(f"   Union : {union_result}")
print(f"   Intersection : {intersection_result}\n")



student_record = {
    "name": "Abdullah",
    "roll_no": 305,
    "age": 20,
    "Degree": "Computer Science",
    "marks": {"Math": 88, "Physics": 92, "English": 95}
}
print("1. Student Record Dictionary:")
for key, value in student_record.items():
    print(f"   {key.capitalize()}: {value}")
print()


students_marks = {
    "Alice": 85.5,
    "Bob": 90.0,
    "Charlie": 78.0,
    "Diana": 92.5,
    "Ethan": 88.0
}

total_marks = 0
for name, score in students_marks.items():
    total_marks += score

avg_score = total_marks / len(students_marks)
print(f"2. Student Marks: {students_marks}")
print(f"   Average Marks across all students: {avg_score:.2f}\n")


sentence = "My name is Muhammad Abdullah Ismail and i am enjoying my internship at ML Bench"
words = sentence.split()
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print(f"3. Sentence: '{sentence}'")
print("   Word Frequencies:")
for word, freq in word_freq.items():
    print(f"   - '{word}': {freq}")


