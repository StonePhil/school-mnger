

```markdown
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


school_management_system/
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


## Requirements

- Python 3.8 or higher
- MySQL Server (8.0+ recommended)

### Python Dependencies

No external Python packages are required (only built-in + `mysql-connector-python`).

## Setup Instructions

### 1. Clone or Download the Project

```bash
git clone <your-repo-url>
cd school_management_system
```

### 2. Install MySQL Connector

```bash
pip install mysql-connector-python
```

### 3. Create `requirements.txt`

Create a file named `requirements.txt` in the project root with the following content:

```txt
mysql-connector-python
```

You can also generate it automatically by running:

```bash
pip freeze > requirements.txt
```

### 4. Database Configuration

Update `config.py` if needed:
- Default credentials: `root` / `C0ventryCUC`
- Change `HOST`, `USER`, or `PASSWORD` as per your MySQL setup.

Make sure MySQL server is running.

### 5. Run the Application

```bash
python main.py
```

The application will automatically:
- Create the database `MY_SCHOOL_DATABASE` if it doesn't exist
- Create all required tables with proper constraints
- Start the interactive menu

## How to Use

- Choose options from the main menu (1–5)
- Navigate through sub-menus for Students, Teachers, Courses, and Enrollments
- Use option 4 in Student Management to see **search** and **sorting** in action
- Enter `5` in the main menu to exit

## Notes

- All inputs are validated
- Database changes are committed automatically on successful operations
- Foreign key constraints ensure referential integrity (e.g., cannot delete a teacher assigned to a course without handling)

---

**Enjoy using the School Management System!**

```

---

### Bonus: You can also create the `requirements.txt` file with just this content:

**`requirements.txt`**

```txt
mysql-connector-python
```

