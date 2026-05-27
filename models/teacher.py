from models.person import Person


class Teacher(Person):
    #teacher model

    def print_details(self):
        print(f"ID: {self.person_id or 'N/A'}, Name: {self.name}, "
              f"Email: {self.email or 'N/A'}  (Role: Teacher)")
