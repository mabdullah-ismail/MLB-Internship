import os
import json

# Relative path so it works reliably in any environment
FILE_PATH = os.path.join("Day4", "data.json")

data = [ 
    {
        "Name": "Abdullah",
        "Roll Number": "100-A",
        "Course": "Computer Engineering",
        "Age": 17
    },
    {
        "Name": "Ali",
        "Roll Number": "101-B",
        "Course": "Computer Engineering",
        "Age": 18
    }
]


with open(FILE_PATH, "w") as f:
    json.dump(data, f, indent=4)  


with open(FILE_PATH, "r") as f:
    data = json.load(f)
    print("Initial Data:")
    print(data)


def add_student(new_student):
    with open(FILE_PATH, "r") as f:
        data = json.load(f)

    data.append(new_student)  

    with open(FILE_PATH, "w") as f:  
        json.dump(data, f, indent=4)

new_data = {
    "Name": "Usman",
    "Roll Number": "2027-C",
    "Course": "Computer Engineering",
    "Age": 19
}

add_student(new_data)


with open(FILE_PATH, "r") as f:
    print("\nUpdated Data after adding Usman:")
    print(json.load(f))
