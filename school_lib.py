import os


USER_FILE    = "users.txt"
STUDENT_FILE = "students.txt"
TEMP_FILE    = "temp.txt"

def make_user(username, password, role, phone, status):
    return {
        "username": username,
        "password": password,
        "role":     role,
        "phone":    phone,
        "status":   status
    }

def make_student(id, name, grade, average_score):
    return {
        "id":            id,
        "name":          name,
        "grade":         grade,
        "average_score": average_score
    }


# -------------------------
# -- -- -- -- -- Valdiating
# -------------------------
def is_valid_phone(phone):
    if len(phone) != 9:
        return False

    prefix = phone[0:2]
    if prefix not in ["77", "73", "71", "78", "70"]:
        return False

    if not phone.isdigit():
        return False

    return True

# --------------------------------
def is_valid_username(username):
    for char in username:
        if char.isdigit() or char in "!@#$%^&*()_+-=[]{}|;':\",./<>?`~\\":
            return False
    return True

# --------------------------------
def is_numeric(input_str):
    return input_str.isdigit()

# --------------------------------
def username_exists(target_user):
    try:
        with open(USER_FILE, "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 5 and parts[0] == target_user:
                    return True
    except FileNotFoundError:
        return False
    return False

# --------------------------------
def is_valid_id(target_id):
    try:
        with open(STUDENT_FILE, "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 4 and int(parts[0]) == target_id:
                    return True
    except FileNotFoundError:
        return False
    return False


# --------------------
# -- -- -- -- -- Login
# --------------------
def login():
    print("\n========================================")
    print("          SYSTEM LOGIN                  ")
    print("========================================")
    in_user = input("Username: ")
    in_pass = input("Password: ")

    # Auto-setup: if file doesn't exist, create default admin
    try:
        f = open(USER_FILE, "r")
        f.close()
    except FileNotFoundError:
        print("[System]: Setup Mode. Creating default Admin.")
        print("[System]: User: admin | Pass: 1234")
        with open(USER_FILE, "w") as f:
            f.write("admin 1234 Admin 770000000 active\n")
        return "Admin"


    with open(USER_FILE, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 5:
                u, p, r, ph, s = parts
                if u == in_user and p == in_pass:
                    if s == "active":
                        return r
                    else:
                        print("\nError: This account is inactive. Contact Admin.")
                        return ""

    print("\nError: Invalid Username or Password.")
    return ""


# -----------------------------
# -- -- -- -- -- Admin Features
# -----------------------------
def add_user():
    print("--Add A New User--")
    username = input("Enter a username: ")

    if not is_valid_username(username):
        print("ERROR! Username must not contain numbers or symbols.")
        return

    if username_exists(username):
        print("Username already exists.")
        return

    password = input("Enter Password: ")
    role     = input("Enter Role (Admin/Employee): ")
    phone    = input("Enter Phone: ")

    if not is_valid_phone(phone):
        print("Error: Invalid phone (Must be 9 digits, start with 7x).")
        return

    status = "active"

    with open(USER_FILE, "a") as f:
        f.write(f"{username} {password} {role} {phone} {status}\n")

    print("User added successfully!")

# --------------------------------
def remove_user():
    target_user = input("Enter username to delete: ")

    found = False
    kept_lines = []

    with open(USER_FILE, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 5 and parts[0] == target_user:
                found = True
            else:
                kept_lines.append(line)

    with open(USER_FILE, "w") as f:
        f.writelines(kept_lines)

    if found:
        print("User deleted.")
    else:
        print("User not found.")

# --------------------------------
def toggle_user_status():
    target_user = input("Enter username to toggle: ")

    found = False
    new_lines = []

    with open(USER_FILE, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 5 and parts[0] == target_user:
                found = True
                parts[4] = "inactive" if parts[4] == "active" else "active"
                print(f"Status changed to: {parts[4]}")
            new_lines.append(" ".join(parts) + "\n")

    with open(USER_FILE, "w") as f:
        f.writelines(new_lines)

    if not found:
        print("User not found.")

# --------------------------------
def view_statistics():
    u_count = 0
    s_count = 0

    try:
        with open(USER_FILE, "r") as f:
            u_count = sum(1 for line in f if line.strip())
    except FileNotFoundError:
        pass

    try:
        with open(STUDENT_FILE, "r") as f:
            s_count = sum(1 for line in f if line.strip())
    except FileNotFoundError:
        pass

    print("\n--- Statistics ---")
    print(f"Total Users:    {u_count}")
    print(f"Total Students: {s_count}")


# --------------------------------
# -- -- -- -- -- Employee Features
# --------------------------------

def add_student_record():
    print("--Add A New Student Record--")

    id_input = input("Enter Student ID: ")
    if not id_input.isdigit():
        print("Error: ID must be a number.")
        return
    student_id = int(id_input)

    if is_valid_id(student_id):
        print("Student ID already exists.")
        return

    name  = input("Enter Student Name: ")
    grade = input("Enter Student Grade: ")

    score_input = input("Enter Student Average Score: ")
    try:
        score = float(score_input)
    except ValueError:
        print("Error: Score must be a number.")
        return

    with open(STUDENT_FILE, "a") as f:
        f.write(f"{student_id} {name} {grade} {score}\n")

    print("Student record added successfully!")

# --------------------------------
def search_student():
    print("--Search A Student--")

    id_input = input("Enter a student ID: ")
    if not id_input.isdigit():
        print("Error: ID must be a number.")
        return
    student_id = int(id_input)

    try:
        with open(STUDENT_FILE, "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 4 and int(parts[0]) == student_id:
                    print("\n--- Student Found ---")
                    print(f"ID:    {parts[0]}")
                    print(f"Name:  {parts[1]}")
                    print(f"Grade: {parts[2]}")
                    print(f"Score: {parts[3]}")
                    return
    except FileNotFoundError:
        print("Error: No student records found.")
        return

    print("Student not found.")

# --------------------------------
def delete_student():
    print("--Delete A Student--")

    id_input = input("Enter student ID: ")
    if not id_input.isdigit():
        print("Error: ID must be a number.")
        return
    student_id = int(id_input)

    found = False
    kept_lines = []

    try:
        with open(STUDENT_FILE, "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 4 and int(parts[0]) == student_id:
                    found = True
                else:
                    kept_lines.append(line)
    except FileNotFoundError:
        print("Error: No student records found.")
        return

    with open(STUDENT_FILE, "w") as f:
        f.writelines(kept_lines)

    if found:
        print("Student deleted.")
    else:
        print("Student not found.")

# --------------------------------
def update_student():
    print("--Update A Student--")

    id_input = input("Enter student ID: ")
    if not id_input.isdigit():
        print("Error: ID must be a number.")
        return
    student_id = int(id_input)

    found = False
    new_lines = []

    try:
        with open(STUDENT_FILE, "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 4 and int(parts[0]) == student_id:
                    found = True
                    print(f"Current Name:  {parts[1]}")
                    print(f"Current Grade: {parts[2]}")
                    print(f"Current Score: {parts[3]}")

                    new_name  = input("Enter New Name: ")
                    new_grade = input("Enter New Grade: ")
                    new_score = input("Enter New Score: ")

                    try:
                        float(new_score)
                    except ValueError:
                        print("Error: Score must be a number.")
                        return

                    new_lines.append(f"{parts[0]} {new_name} {new_grade} {new_score}\n")
                else:
                    new_lines.append(line)
    except FileNotFoundError:
        print("Error: No student records found.")
        return

    with open(STUDENT_FILE, "w") as f:
        f.writelines(new_lines)

    if found:
        print("Student updated successfully.")
    else:
        print("Student ID not found.")

# --------------------------------
def generate_report():
    students = []

    try:
        with open(STUDENT_FILE, "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 4:
                    students.append(make_student(
                        id           = int(parts[0]),
                        name         = parts[1],
                        grade        = parts[2],
                        average_score= float(parts[3])
                    ))
    except FileNotFoundError:
        print("Error: No records found.")
        return

    if len(students) == 0:
        print("No student records to display.")
        return

    print("\n--- Academic Report ---")
    print(f"{'Name':<15} {'Grade':<10} {'Score'}")
    print("------------------------------------")

    for student in students:
        print(f"{student['name']:<15} {student['grade']:<10} {student['average_score']}")

    print("------------------------------------")
    print("\n        GRADE STATISTICS")
    print("------------------------------------")

    # track which grades we already counted
    seen_grades = []

    for student in students:
        current_grade = student["grade"]
        if current_grade not in seen_grades:
            seen_grades.append(current_grade)
            grade_count = sum(1 for s in students if s["grade"] == current_grade)
            print(f"Grade {current_grade}: {grade_count} student(s)")

    print("====================================")

    