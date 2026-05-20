```markdown
# School Management System

A robust, object-oriented Python application for managing a school database with full CRUD operations, secure login, and role-based authorization.

## Features

- **Secure Login System** with Authentication (bcrypt hashing)
- **Role-based Authorization** (Admin & Teacher roles)
- Proper OOP Design (Inheritance, Encapsulation)
- Normalized 3NF Database with constraints (PK, FK, UNIQUE, CHECK, DEFAULT, INDEX)
- Full CRUD for Students, Teachers, Courses, and Enrollments
- Search (Linear Search) and Sorting (Bubble Sort) algorithms
- Input validation and comprehensive error handling
- Follows PEP 8 standards with detailed comments

## Project Structure

```text
school_management_system/
├── main.py
├── config.py
├── requirements.txt
├── database/
│   └── connection.py
├── models/
│   ├── __init__.py
│   ├── person.py
│   ├── student.py
│   ├── teacher.py
│   ├── course.py
│   └── enrollment.py
├── utils/
│   ├── __init__.py
│   ├── validators.py
│   └── helpers.py
└── auth/
    ├── __init__.py
    └── auth_manager.py
```

## Requirements

- Python 3.8 or higher
- MariaDB / MySQL Server

### Python Dependencies

`requirements.txt` is included in the repository.

## Setup Instructions

### For Linux

1. **Clone or navigate to project folder:**
   ```bash
   cd ~/Desktop/school-mnger
   ```

2. **Install MySQL/MariaDB Connector and bcrypt:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start Database Server:**
   ```bash
   # On Fedora
   sudo systemctl start mysqld
   # OR on Ubuntu/Debian
   sudo systemctl start mysql
   ```

4. **Run the Application:**
   ```bash
   python3 main.py
   ```

---

### For Windows

1. **Open Command Prompt or PowerShell** and navigate to project folder:
   ```cmd
   cd Desktop\school-mnger
   ```

2. **Install dependencies:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Make sure MySQL Server is running** (usually starts automatically, or start via XAMPP / MySQL Workbench).

4. **Run the Application:**
   ```cmd
   python main.py
   ```

---

## Default Login Credentials

After first run, a default admin account is automatically created:

- **Username:** `admin`
- **Password:** `admin123`

**Important:** Change the default password after first login for security.

## How to Use

1. Run the program → Login screen appears
2. Login with credentials
3. Use the main menu (options 1–7)
4. **Admins** have full access
5. **Teachers** have limited access
6. Use option `6` to logout and login with another account
7. Use option `7` to exit

## Notes

- The system creates the database `MY_SCHOOL_DATABASE` and all tables automatically on first run.
- All passwords are securely hashed using bcrypt.
- Foreign key constraints maintain data integrity.
- For Fedora users: Use `mariadb` or `mysqld` service name.
