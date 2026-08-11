

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def check_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def count_digits(number):
    return len(str(abs(number)))


def reverse_number(number):
    reversed_val = 0
    temp = abs(number)

    while temp > 0:
        remainder = temp % 10
        reversed_val = (reversed_val * 10) + remainder
        temp = temp // 10

    if number < 0:
        reversed_val = -reversed_val

    return reversed_val


def check_palindrome(number):
    if number < 0:
        return False
    return number == reverse_number(number)


def generate_fibonacci(terms):
    if terms <= 0:
        return []
    elif terms == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < terms:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)

    return sequence


def analyze_number():
    try:
        number = int(input("Enter a number to analyze: ").strip())

        print("\nNumber Analysis")
        print("Number          :", number)
        print("Even / Odd      :", check_even_odd(number))
        print("Prime Number    :", "Yes" if check_prime(number) else "No")
        print("Total Digits    :", count_digits(number))
        print("Reversed Number :", reverse_number(number))
        print("Palindrome      :", "Yes" if check_palindrome(number) else "No")
       
    except ValueError:
        print("[!] Please enter a valid integer.")


def run_prime_checker():
    try:
        number = int(input("Enter a number to check prime: ").strip())
        if check_prime(number):
            print(f"[+] {number} is a Prime Number.")
        else:
            print(f"[-] {number} is NOT a Prime Number.")
    except ValueError:
        print("[!] Please enter a valid integer.")


def run_fibonacci_generator():
    try:
        terms = int(input("Enter number of Fibonacci terms: ").strip())
        if terms <= 0:
            print("[!] Number of terms must be greater than 0.")
        else:
            fib_series = generate_fibonacci(terms)
            print(f"[+] Fibonacci Series ({terms} terms): {fib_series}")
    except ValueError:
        print("[!] Please enter a valid integer.")


def run_palindrome_checker():
    try:
        number = int(input("Enter a number to check palindrome: ").strip())
        if check_palindrome(number):
            print(f"[+] {number} is a Palindrome.")
        else:
            print(f"[-] {number} is NOT a Palindrome.")
    except ValueError:
        print("[!] Please enter a valid integer.")


def run_multiplication_table():
    try:
        number = int(input("Enter a number for multiplication table: ").strip())
        print(f"\n--- Multiplication Table of {number} ---")
        for i in range(1, 11):
            print(f"{number} x {i:<2} = {number * i}")
    except ValueError:
        print("[!] Please enter a valid integer.")


def main():
    while True:
        print("\nNumber Analysis & Problem Solver Tool")
        print("1. Analyze a Number")
        print("2. Check Prime Number")
        print("3. Generate Fibonacci Series")
        print("4. Check Palindrome Number")
        print("5. Multiplication Table Generator")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            analyze_number()
        elif choice == "2":
            run_prime_checker()
        elif choice == "3":
            run_fibonacci_generator()
        elif choice == "4":
            run_palindrome_checker()
        elif choice == "5":
            run_multiplication_table()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("[!] Invalid choice. Please select 1 to 6.")


if __name__ == "__main__":
    main()
