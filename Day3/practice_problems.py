num1 = -15
if num1 > 0:
    result1 = "Positive"
elif num1 < 0:
    result1 = "Negative"
else:
    result1 = "Zero"
print(f"1. Number: {num1} | Result: {result1}")


num2 = 28
if num2 % 2 == 0:
    result2 = "Even"
else:
    result2 = "Odd"
print(f"2. Number: {num2} | Result: {result2}")


marks = 85.5
if marks >= 90:
    grade = "A (Excellent)"
elif marks >= 80:
    grade = "B (Very Good)"
elif marks >= 70:
    grade = "C (Good)"
elif marks >= 60:
    grade = "D (Satisfactory)"
else:
    grade = "F (Fail)"
print(f"3. Marks: {marks} | Grade: {grade}")


a, b, c = 45, 89, 23
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print(f"4. Numbers: ({a}, {b}, {c}) | Largest: {largest}")

year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    is_leap = True
else:
    is_leap = False
print(f"5. Year: {year} | Leap Year: {is_leap}\n")


print("1. All numbers from 1 to 100:")
for i in range(1, 101):
    print(i, end=" ")
print("\n")

print("2. All even numbers from 1 to 100:")
for i in range(1, 101):
    if i % 2 == 0:
        print(i, end=" ")
print("\n")


n = 50
total_sum = 0
for i in range(1, n + 1):
    total_sum += i
print(f"3. Sum of numbers from 1 to {n}: {total_sum}")


table_num = 7
print(f"4. Multiplication Table of {table_num}:")
for i in range(1, 11):
    print(f"   {table_num} x {i:<2} = {table_num * i}")


digit_num = 9876543
temp_num = abs(digit_num)
digit_count = 0
if temp_num == 0:
    digit_count = 1
else:
    while temp_num > 0:
        digit_count += 1
        temp_num //= 10
print(f"5. Number: {digit_num} | Total Digits: {digit_count}\n")



orig_num = 12345
num_to_rev = abs(orig_num)
reversed_num = 0
while num_to_rev > 0:
    remainder = num_to_rev % 10
    reversed_num = (reversed_num * 10) + remainder
    num_to_rev //= 10

if orig_num < 0:
    reversed_num = -reversed_num

print(f"1. Original Number: {orig_num} | Reversed Number: {reversed_num}")


pal_num = 12321
str_pal = str(abs(pal_num))
if str_pal == str_pal[::-1]:
    is_pal = True
else:
    is_pal = False
print(f"2. Number: {pal_num} | Palindrome: {is_pal}")


fib_terms = 10
fib_sequence = []
a_fib, b_fib = 0, 1
for _ in range(fib_terms):
    fib_sequence.append(a_fib)
    a_fib, b_fib = b_fib, a_fib + b_fib
print(f"3. Fibonacci sequence ({fib_terms} terms): {fib_sequence}")


prime_test_num = 29
is_prime = True
if prime_test_num <= 1:
    is_prime = False
else:
    for i in range(2, int(prime_test_num ** 0.5) + 1):
        if prime_test_num % i == 0:
            is_prime = False
            break
print(f"4. Number: {prime_test_num} | Prime: {is_prime}")


primes_1_to_100 = []
for val in range(2, 101):
    val_is_prime = True
    for divisor in range(2, int(val ** 0.5) + 1):
        if val % divisor == 0:
            val_is_prime = False
            break
    if val_is_prime:
        primes_1_to_100.append(val)

print(f"5. Prime numbers between 1 and 100 ({len(primes_1_to_100)} total):")
print(f"   {primes_1_to_100}")
