import random
import string
import json

# Function to generate random grades between 0 and 130
def generate_grades():
    return [random.randint(0, 130) for _ in range(10)]

# Function to generate random class in the format 'class-<capital_letter>'
def generate_class():
    return f"class-{random.choice(string.ascii_uppercase)}"

# Function to generate a single student
def generate_student(student_id):
    student = {
        "id": student_id,
        "name": f"Student-{student_id}",
        "grades": generate_grades(),
        "class": generate_class() if random.random() > 0.1 else None  # 10% chance of missing the class property
    }
    # Remove the class key if it's None (some students won't have a class)
    if student["class"] is None:
        del student["class"]
    return student

# Function to generate student data with intentional errors
def generate_students(count):
    students = []
    id_list = set()  # To keep track of unique IDs
    for i in range(count):
        student_id = f"{i:03d}"  # Ensure IDs are strings
        student = generate_student(student_id)
        students.append(student)
        id_list.add(student_id)

        # Intentionally add some duplicates (10% duplicates)
        if random.random() > 0.9:
            students.append(student)

    # Ensure that the total number of students is at least 500
    while len(students) < 500:
        # Add some random duplicates to ensure we hit 500 entries
        student_id = random.choice(list(id_list))
        student = generate_student(student_id)
        students.append(student)

    return students

# Generate the students array
students_data = generate_students(500)

# Output to a JSON file
with open('students.json', 'w') as f:
    json.dump(students_data, f, indent=2)

print("Generated students.json file with over 500 students.")
