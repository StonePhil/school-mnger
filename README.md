

# School Management System

A robust, object-oriented Python application for managing a school database with full CRUD operations for Students, Teachers, Courses, and Student Enrollments (Registrations).

## Features

- **Proper OOP Design**: Inheritance, Encapsulation, and Abstraction
- **Normalized Database (3NF)**: Students, Teachers, Courses, and Enrollments with proper constraints (PK, FK, UNIQUE, CHECK, DEFAULT, INDEX)
- **Full CRUD** operations for all entities
- **Search & Sorting Algorithms**: Linear Search + Bubble Sort
- **Input Validation** and comprehensive **Error Handling**
- **Persistent Menu Loop** – program runs until user quits
- Follows **PEP 8** standards with detailed code comments

## Project Structure

```markdown
school-mnger/
├── main.py
├── config.py
├── database/
│   └── connection.py
├── models/
│   ├── __init__.py
│   ├── person.py
│   ├── student.py
│   ├── teacher.py
│   ├── course.py
│   └── enrollment.py
└── utils/
    ├── __init__.py
    ├── validators.py
    └── helpers.py
```

## Requirements

- Python 3.8 or higher
- MariaDB / MySQL Server

### Python Dependencies

`requirements.txt` is already included in the repository.

To install dependencies:

```bash
pip install -r requirements.txt
```

## Setup Instructions

### 1. Clone or Download the Project

```bash
git clone https://github.com/StonePhil/school-mnger
cd school_management_system
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Database Configuration

- Default credentials in `config.py`: `root` / `C0ventryCUC`
- Make sure MariaDB/MySQL server is running:

```bash
sudo systemctl start mysqld    # or mariadb on Fedora
```

- Update `config.py` only if your username, password, or host is different.

### 4. Run the Application

```bash
python3 main.py
```

The application will automatically:
- Create the database `MY_SCHOOL_DATABASE` if it doesn't exist
- Create all required tables with proper constraints
- Start the interactive menu

## How to Use

- Choose options from the main menu (1–5)
- Navigate through sub-menus for **Students**, **Teachers**, **Courses**, and **Enrollments**
- In **Student Management**, use option 4 to see **search** and **sorting** in action
- Enter `5` in the main menu to exit

## Notes

- All user inputs are validated
- Database changes are committed automatically on successful operations
- Foreign key constraints ensure referential integrity

---
