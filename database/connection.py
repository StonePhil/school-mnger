import mysql.connector
from mysql.connector import errorcode
import sys
from config import DB_NAME, USER, PASSWORD, HOST


class DBConnection:
    #encapsulates mysql connection and provides safe query execution

    def __init__(self):
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        #establish connection and ensure database+tables exist
        try:
            self.connection = mysql.connector.connect(
                user=USER, password=PASSWORD, host=HOST
            )
            self.cursor = self.connection.cursor()
            self._ensure_database_exists()
            self.connection.database = DB_NAME
            self._create_tables()
        except mysql.connector.Error as err:
            print(f"Database connection failed: {err}")
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Please check your MySQL username and password.")
            sys.exit(1)

    def _ensure_database_exists(self):
        try:
            self.cursor.execute(f"USE {DB_NAME}")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(
                    f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8mb4'"
                )
                print(f"Database '{DB_NAME}' created successfully.")
                self.connection.commit()
            else:
                raise

    def _create_tables(self):
        #creates normalized 3nf tables with proper constraints
        tables = [
            # Teachers
            """
            CREATE TABLE IF NOT EXISTS Teachers (
                TeacherID INT PRIMARY KEY AUTO_INCREMENT,
                TeacherName VARCHAR(100) NOT NULL,
                Email VARCHAR(100) UNIQUE,
                INDEX idx_teacher_name (TeacherName)
            )
            """,
            # Students
            """
            CREATE TABLE IF NOT EXISTS Students (
                StudentID INT PRIMARY KEY AUTO_INCREMENT,
                StudentName VARCHAR(100) NOT NULL,
                Email VARCHAR(100) UNIQUE,
                DateOfBirth DATE,
                INDEX idx_student_name (StudentName)
            )
            """,
            # Courses
            """
            CREATE TABLE IF NOT EXISTS Courses (
                CourseID INT PRIMARY KEY AUTO_INCREMENT,
                CourseName VARCHAR(100) NOT NULL,
                CourseDetails TEXT,
                TeacherID INT,
                Credits INT DEFAULT 3 CHECK (Credits BETWEEN 1 AND 6),
                FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID) ON DELETE SET NULL,
                INDEX idx_course_name (CourseName)
            )
            """,
            # Enrollments
            """
            CREATE TABLE IF NOT EXISTS Enrollments (
                EnrollmentID INT PRIMARY KEY AUTO_INCREMENT,
                StudentID INT NOT NULL,
                CourseID INT NOT NULL,
                RegistrationDate DATE DEFAULT (CURRENT_DATE),
                FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE,
                FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE,
                UNIQUE KEY unique_enrollment (StudentID, CourseID)
            )
            """
        ]

        for sql in tables:
            self.cursor.execute(sql)
        self.connection.commit()
        print("All tables created successfully (3NF normalized database).")

    def execute_query(self, query: str, params: tuple = None):
        #execute query with parameters and commit
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Query error: {err}")
            self.connection.rollback()
            raise

    def fetch_all(self, query: str, params: tuple = None):
        #fetch all results safely
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Fetch error: {err}")
            raise

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
