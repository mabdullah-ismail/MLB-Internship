# Day 5: Object-Oriented Programming (OOP) & Library Management System

Welcome to **Day 5** of the MLB Internship curriculum! Today's focus is on mastering **Object-Oriented Programming (OOP)** concepts, **Inheritance**, **Encapsulation**, and building a persistent **Console-based Library Management System**.

---

## 💡 What is Object-Oriented Programming (OOP)?
Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around **data (objects)** and **behaviors (methods)** rather than functions and linear logic.
- **Classes**: Blueprints or templates used to create objects (e.g. `Book`, `Student`).
- **Objects**: Specific instances of a class containing real data (e.g. `c1 = Car("Toyota", "Camry", 2023)`).
- **Encapsulation**: Bundling data and methods into a single unit while restricting direct access to internal states using private attributes (`__salary`, `__gpa`) and getters/setters.
- **Inheritance**: Allowing a child class to inherit attributes and methods from a parent class (`Student` & `Teacher` inheriting from `Person`).

---

## 🧬 Where Inheritance Was Used in the Project

In the **Library Management System** ([library_management_system.py](file:///d:/MLB-Internship/Day%205/library_management_system.py)):
1. **Base Class (`LibraryItem`)**: Defines common attributes (`item_id`, `title`, `author`, `is_borrowed`, `borrowed_by`) and basic borrowing/returning behaviors.
2. **Derived Class (`Book`)**: Inherits all features from `LibraryItem` using `super().__init__()` and adds book-specific attributes like `isbn` and `genre`.
3. **Method Overriding**: `Book` overrides `display_details()` and `to_dict()` to include ISBN and genre details while retaining the core logic of `LibraryItem`.

In the **OOP Practice Script** ([oop_practice.py](file:///d:/MLB-Internship/Day%205/oop_practice.py)):
- `Person` serves as a parent class with `name`, `age`, `email`.
- `StudentMember` and `Teacher` inherit from `Person`, overriding `display_info()` to include GPA and salary details respectively.

---

## 🛠️ Practice Tasks & Scripts

### 1. OOP Practice Script ([oop_practice.py](file:///d:/MLB-Internship/Day%205/oop_practice.py))
- Demonstrates `Student`, `Employee`, and `Car` classes with multiple object instances.
- Demonstrates parent/child inheritance (`Person` -> `StudentMember` / `Teacher`).
- Demonstrates encapsulation with private attributes (`__gpa`, `__salary`) and getters/setters.

### 2. Library Management System ([library_management_system.py](file:///d:/MLB-Internship/Day%205/library_management_system.py))
- **Add Book**: Insert new records with automatic ID generation (`BOK-001`) and duplicate ISBN checks.
- **View All Books**: View formatted library catalog with availability statuses.
- **Search Book**: Search by Title, Author, ISBN, or Item ID.
- **Borrow & Return**: Change book availability status and track borrower names.
- **Data Persistence**: Automatically synchronizes all changes to [library_data.json](file:///d:/MLB-Internship/Day%205/library_data.json).

---

## 💡 Challenges Faced & Solutions

1. **Serializing Custom Objects to JSON**:
   - **Challenge**: JSON cannot natively serialize Python class instances (`TypeError: Object of type Book is not JSON serializable`).
   - **Solution**: Implemented `.to_dict()` instance methods and `.from_dict()` class methods on `Book` and `LibraryItem` to convert between custom Python objects and JSON-compatible dictionaries.

2. **Handling Inheritance in Dictionary Conversions**:
   - **Challenge**: Converting derived objects into dictionaries without repeating parent attribute mappings.
   - **Solution**: Used `data = super().to_dict()` inside `Book.to_dict()` to cleanly combine parent dictionary keys with child-specific fields (`isbn`, `genre`).

3. **Input Validation & Exception Handling**:
   - **Challenge**: Invalid CLI choices, empty search queries, or missing JSON data files could crash the application.
   - **Solution**: Wrapped CLI input loops and JSON file loading in `try...except` blocks (`json.JSONDecodeError`, `IOError`) with user-friendly error messages.

---

## 💻 How to Run

### 1. Run OOP Practice Script
```bash
python "Day 5/oop_practice.py"
```

### 2. Run Library Management System
```bash
python "Day 5/library_management_system.py"
```
