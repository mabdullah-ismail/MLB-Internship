# Day 5: Object-Oriented Programming (OOP) & Library Management System


## What is Object-Oriented Programming (OOP)?
Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around **data (objects)** and **behaviors (methods)** rather than functions and linear logic.
- **Classes**: Blueprints or templates used to create objects (e.g. `Book`, `Student`).
- **Objects**: Specific instances of a class containing real data (e.g. `c1 = Car("Toyota", "Camry", 2023)`).
- **Encapsulation**: Bundling data and methods into a single unit while restricting direct access to internal states using private attributes (`__salary`, `__gpa`) and getters/setters.
- **Inheritance**: Allowing a child class to inherit attributes and methods from a parent class (`Student` & `Teacher` inheriting from `Person`).



##  Where Inheritance Was Used in the Project

In the **Library Management System** ([library_management_system.py](file:///d:/MLB-Internship/Day%205/library_management_system.py)):
1. **Base Class (`LibraryItem`)**: Defines common attributes (`item_id`, `title`, `author`, `is_borrowed`, `borrowed_by`) and basic borrowing/returning behaviors.
2. **Derived Class (`Book`)**: Inherits all features from `LibraryItem` using `super().__init__()` and adds book-specific attributes like `isbn` and `genre`.
3. **Method Overriding**: `Book` overrides `display_details()` and `to_dict()` to include ISBN and genre details while retaining the core logic of `LibraryItem`.

In the **OOP Practice Script** ([oop_practice.py](file:///d:/MLB-Internship/Day%205/oop_practice.py)):
- `Person` serves as a parent class with `name`, `age`, `email`.
- `StudentMember` and `Teacher` inherit from `Person`, overriding `display_info()` to include GPA and salary details respectively.

---

##  Practice Tasks & Scripts

### 1. OOP Practice Script ([oop_practice.py](file:///d:/MLB-Internship/Day%205/oop_practice.py))

### 2. Library Management System ([library_management_system.py](file:///d:/MLB-Internship/Day%205/library_management_system.py))


##  How to Run

### 1. Run OOP Practice Script
```bash
python "Day 5/oop_practice.py"
```

### 2. Run Library Management System
```bash
python "Day 5/library_management_system.py"
```
