from models.person import Person


class Student(Person):
    #Student model with inheritance

    def __init__(self, student_id=None, name="", email=None, date_of_birth=None):
        super().__init__(student_id, name, email)
        self._date_of_birth = date_of_birth

    @property
    def date_of_birth(self):
        return self._date_of_birth

    def print_details(self):
        super().print_details()
        print(f"ID: {self.person_id or 'N/A'}, Name: {self.name}, "
              f"Email: {self.email or 'N/A'}")
        if self.date_of_birth:
            print(f"  Date of Birth: {self.date_of_birth}")
