class Course:
    #Course entity

    def __init__(self, course_id=None, name="", details="", teacher_id=None, credits=3):
        self._course_id = course_id
        self._name = name.strip()
        self._details = details
        self._teacher_id = teacher_id
        self._credits = credits

    @property
    def course_id(self):
        return self._course_id

    @property
    def name(self):
        return self._name

    def print_details(self):
        print(f"Course ID: {self.course_id or 'N/A'}, Name: {self.name}, "
              f"Credits: {self._credits}, TeacherID: {self._teacher_id or 'N/A'}")
        if self._details:
            print(f"  Details: {self._details}")
