```markdown
# School Management System

A robust, object-oriented Python application for managing a school database with full CRUD operations for Students, Teachers, Courses, and Student Enrollments.

## Features

- Proper OOP Design (Inheritance, Encapsulation)
- Normalized 3NF Database with constraints (PK, FK, UNIQUE, CHECK, DEFAULT, INDEX)
- Full CRUD for Students, Teachers, Courses, and Enrollments
- Search (Linear Search) and Sorting (Bubble Sort) algorithms
- Input validation and comprehensive error handling
- Persistent menu loop until user quits
- Follows PEP 8 standards with detailed comments

## Project Structure

```
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
```

## Requirements

- Python 3.8+
- MySQL Server

### Python Dependencies

```txt
mysql-connector-python
```

## Setup Instructions

1. **Create the project folder structure** as shown above and place each file with the corresponding code.

2. **Install the required package:**

```bash
pip install mysql-connector-python
```

3. **Create `requirements.txt`** in the project root with the following content:

```txt
mysql-connector-python
```

4. **Configure Database** (optional):
   - Open `config.py`
   - Update `USER`, `PASSWORD`, or `HOST` if different from defaults (`root` / `C0ventryCUC` / `localhost`)

5. **Run the application:**

```bash
python main.py
```

The program will automatically create the database `MY_SCHOOL_DATABASE` and all tables on first run.

## Usage

- Select options from the main menu (1-5)
- Use sub-menus to perform CRUD operations
- In Student Management → Option 4 demonstrates search and sorting
- Enter `5` in the main menu to exit

## Notes

- All user inputs are validated
- Database operations include proper error handling and rollback on failure
- Referential integrity is enforced via foreign keys

Enjoy using the School Management System!
```
