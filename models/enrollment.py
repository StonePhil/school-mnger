class Enrollment:
    """Enrollment between Student and Course."""

    def __init__(self, enrollment_id=None, student_id=0, course_id=0, registration_date=None):
        self._enrollment_id = enrollment_id
        self._student_id = student_id
        self._course_id = course_id
        self._registration_date = registration_date

    def print_details(self):
        print(f"EnrollmentID: {self._enrollment_id or 'N/A'}, "
              f"StudentID: {self._student_id}, CourseID: {self._course_id}, "
              f"Date: {self._registration_date}")
