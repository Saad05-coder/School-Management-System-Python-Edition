# 🏫 Python School Management System

A robust, console-based application designed to manage school records, user authentication, and academic reporting. 

This project is a complete rewrite of a previous procedural C++ system, modernized using **Python 3**. By shifting from manual pointers and structs to Python's native data structures and advanced file I/O operations, this application delivers a clean, modular administrative database solution.

## 🚀 Project Overview
The system acts as a localized database for a school environment. It guarantees data persistence across sessions by reading from and writing to flat text files (`users.txt` and `students.txt`), completely removing the requirement for bulky external database engines. 

The application utilizes a secure login system featuring two distinct access tiers: **Admins** and **Employees**.

## ✨ Key Features

### 🔐 Authentication & Form Validation
- **Secure Access Control:** Checks username, password, and account status (`Active`/`Inactive`) before granting console access.
- **Dynamic Initialization:** Automatically generates a default Admin account on the system's first run if no user file is detected.
- **Strict Data Validation:** - Usernames are strictly verified to prevent numbers or special symbols.
  - Phone numbers must be exactly 9 digits and conform to Yemeni provider prefixes (`71`, `73`, `77`, `78`).
  - Implements complete `try-except` blocks to handle input exceptions and protect the terminal interface from crashing due to unexpected input types.

### 👤 Admin Capabilities
- **User Directory Management:** Full control to add and remove system operators (Employees/Admins).
- **Access Toggling:** Instantly flip user status (`Activate`/`Deactivate`) to block system access without deleting any records.
- **System Metrics:** Real-time dashboards displaying the total count of operational users and student records.

### 📚 Employee Capabilities
- **Student Record CRUD:** - **C**reate new student profiles.
  - **R**ead/Search student data instantly via unique IDs.
  - **U**pdate student metrics, grades, and academic scores.
  - **D**elete records dynamically.
- **Academic Matrix Analytics:** Generates formatted tabular reports in the console and dynamically aggregates class distributions (e.g., `"Grade 10: 5 Students"`) utilizing Python's fast dictionary mappings.

## 🛠️ Python Concepts Demonstrated
- **File Architecture:** Utilizing contextual managers (`with open(...)`) for automated, memory-safe file stream lifecycles.
- **Data Collections:** Advanced application of lists, dictionaries, and list comprehensions for real-time searching, filtering, and reporting data processing.
- **String Formatting:** Employs f-strings and text-justification methods to build clean, alignment-precise tabular reports.
- **Exception Handling:** Bulletproofing terminal loops with targeted user input error catching.

## 📦 Local Setup & Execution

### Prerequisites
- Python 3.8 or higher installed on your machine.

### Installation & Execution
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Saad05-coder/School-Management-System-Python-Edition.git](https://github.com/Saad05-coder/School-Management-System-Python-Edition.git)
   cd School-Management-System-Python-Edition

2. **Run the application:**
   ```bash
   python main.py
   (Note: Depending on your global environment configurations, you may need to specify python3 main.py)

## 🔑 Default Credentials
- Upon initialization, use the following credentials to access the primary Administrator dashboard:
  - Username: admin
  - Password: 1234

## 📝 Data Storage Format
- Data is tracked locally in text files using structured layouts, making external backups incredibly simple:
  - `users.txt` pattern: `username,password,role,status`
  - `students.txt` pattern: `id,name,grade,score,phone`
