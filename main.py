from database.connection import DBConnection
from utils.validators import validate_positive_int, validate_non_empty
from utils.helpers import linear_search, bubble_sort
import sys
from datetime import date


class SchoolManagementSystem:
    #main application class with menu interface
    def __init__(self):
        self.db = DBConnection()
        print("School Management System started successfully!\n")

    def _load_students(self):
        return self.db.fetch_all("SELECT StudentID, StudentName, Email, DateOfBirth FROM Students")

    def _load_teachers(self):
        return self.db.fetch_all("SELECT TeacherID, TeacherName, Email FROM Teachers")

    def _load_courses(self):
        return self.db.fetch_all(
            "SELECT CourseID, CourseName, CourseDetails, TeacherID, Credits FROM Courses"
        )

    def _load_enrollments(self):
        return self.db.fetch_all("""
            SELECT e.EnrollmentID, s.StudentName, c.CourseName, e.RegistrationDate
            FROM Enrollments e
            JOIN Students s ON e.StudentID = s.StudentID
            JOIN Courses c ON e.CourseID = c.CourseID
        """)

    # ===================== STUDENT MANAGEMENT =====================
    def manage_students(self):
        while True:
            print("\n=== Student Management ===")
            print("1. Add Student")
            print("2. Update Student")
            print("3. Delete Student")
            print("4. View All Students (Search + Sort)")
            print("5. Back to Main Menu")
            choice = input("Enter choice: ").strip()

            if choice == "1":   # CREATE
                name = validate_non_empty("Student Name: ")
                email = input("Email (optional): ").strip() or None
                dob = input("Date of Birth (YYYY-MM-DD, optional): ").strip() or None
                try:
                    self.db.execute_query(
                        "INSERT INTO Students (StudentName, Email, DateOfBirth) VALUES (%s, %s, %s)",
                        (name, email, dob)
                    )
                    print("Student added successfully!")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "2":  # UPDATE
                sid = validate_positive_int("StudentID to update: ")
                name = validate_non_empty("New Student Name: ")
                try:
                    self.db.execute_query(
                        "UPDATE Students SET StudentName = %s WHERE StudentID = %s",
                        (name, sid)
                    )
                    print("Student updated!")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "3":  # DELETE
                sid = validate_positive_int("StudentID to delete: ")
                try:
                    self.db.execute_query("DELETE FROM Students WHERE StudentID = %s", (sid,))
                    print("Student deleted!")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "4":  # VIEW + SEARCH + SORT
                records = self._load_students()
                if not records:
                    print("No students found.")
                    continue

                print("\nStudents sorted by name (Bubble Sort):")
                sorted_records = bubble_sort(records, 1)  # sort by StudentName
                for row in sorted_records:
                    print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2] or 'N/A'}")

                search = input("\nSearch by name (or press Enter to skip): ").strip()
                if search:
                    results = linear_search(sorted_records, search, 1)
                    print(f"\nFound {len(results)} result(s):")
                    for r in results:
                        print(f"ID: {r[0]}, Name: {r[1]}")

            elif choice == "5":
                break
            else:
                print("Invalid choice. Try again.")

    #TEACHER MANAGEMENT
    def manage_teachers(self):
        while True:
            print("\n=== Teacher Management ===")
            print("1. Add Teacher")
            print("2. Update Teacher")
            print("3. Delete Teacher")
            print("4. View All Teachers")
            print("5. Back")
            choice = input("Enter choice: ").strip()

            if choice == "1":
                name = validate_non_empty("Teacher Name: ")
                email = input("Email (optional): ").strip() or None
                try:
                    self.db.execute_query(
                        "INSERT INTO Teachers (TeacherName, Email) VALUES (%s, %s)",
                        (name, email)
                    )
                    print("Teacher added!")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "2":
                tid = validate_positive_int("TeacherID: ")
                name = validate_non_empty("New Name: ")
                try:
                    self.db.execute_query(
                        "UPDATE Teachers SET TeacherName = %s WHERE TeacherID = %s",
                        (name, tid)
                    )
                    print("Teacher updated!")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "3":
                tid = validate_positive_int("TeacherID to delete: ")
                try:
                    self.db.execute_query("DELETE FROM Teachers WHERE TeacherID = %s", (tid,))
                    print("Teacher deleted!")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "4":
                records = self._load_teachers()
                for row in records:
                    print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2] or 'N/A'}")

            elif choice == "5":
                break

    #COURSE MANAGEMENT
    def manage_courses(self):
        while True:
            print("\n=== Course Management ===")
            print("1. Add Course")
            print("2. Update Course")
            print("3. Delete Course")
            print("4. View All Courses")
            print("5. Back")
            choice = input("Enter choice: ").strip()

            if choice == "1":
                name = validate_non_empty("Course Name: ")
                details = input("Details (optional): ").strip()
                tid = input("TeacherID (optional): ").strip()
                teacher_id = int(tid) if tid.isdigit() else None
                try:
                    self.db.execute_query(
                        "INSERT INTO Courses (CourseName, CourseDetails, TeacherID) VALUES (%s, %s, %s)",
                        (name, details, teacher_id)
                    )
                    print("Course added!")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "2":
                cid = validate_positive_int("CourseID: ")
                name = validate_non_empty("New Course Name: ")
                try:
                    self.db.execute_query(
                        "UPDATE Courses SET CourseName = %s WHERE CourseID = %s",
                        (name, cid)
                    )
                    print("Course updated!")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "3":
                cid = validate_positive_int("CourseID to delete: ")
                try:
                    self.db.execute_query("DELETE FROM Courses WHERE CourseID = %s", (cid,))
                    print("Course deleted!")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "4":
                records = self._load_courses()
                for row in records:
                    print(f"ID: {row[0]}, Name: {row[1]}, TeacherID: {row[3] or 'N/A'}, Credits: {row[4]}")

            elif choice == "5":
                break

    #ENROLLMENT MANAGEMENT
    def manage_enrollments(self):
        while True:
            print("\n=== Enrollment Management ===")
            print("1. Enroll Student in Course")
            print("2. Delete Enrollment")
            print("3. View All Enrollments")
            print("4. Back")
            choice = input("Enter choice: ").strip()

            if choice == "1":
                sid = validate_positive_int("StudentID: ")
                cid = validate_positive_int("CourseID: ")
                try:
                    self.db.execute_query(
                        "INSERT INTO Enrollments (StudentID, CourseID) VALUES (%s, %s)",
                        (sid, cid)
                    )
                    print("Student enrolled successfully!")
                except Exception as e:
                    print(f"Enrollment failed: {e}")

            elif choice == "2":
                eid = validate_positive_int("EnrollmentID to delete: ")
                try:
                    self.db.execute_query("DELETE FROM Enrollments WHERE EnrollmentID = %s", (eid,))
                    print("Enrollment deleted!")
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "3":
                records = self._load_enrollments()
                for row in records:
                    print(f"ID: {row[0]}, Student: {row[1]}, Course: {row[2]}, Date: {row[3]}")

            elif choice == "4":
                break

    def run(self):
        """Main menu loop - program continues until user quits."""
        while True:
            print("\n" + "="*60)
            print("          SCHOOL MANAGEMENT SYSTEM")
            print("="*60)
            print("1. Manage Students")
            print("2. Manage Teachers")
            print("3. Manage Courses")
            print("4. Manage Enrollments / Registrations")
            print("5. Quit Program")
            choice = input("\nEnter your choice (1-5): ").strip()

            if choice == "1":
                self.manage_students()
            elif choice == "2":
                self.manage_teachers()
            elif choice == "3":
                self.manage_courses()
            elif choice == "4":
                self.manage_enrollments()
            elif choice == "5":
                print("\nThank you for using the School Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        self.db.close()


if __name__ == "__main__":
    try:
        app = SchoolManagementSystem()
        app.run()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Database connection closed.")
