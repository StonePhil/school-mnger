from abc import ABC, abstractmethod


class Person(ABC):
    #abstract base class for Student and Teacher

    def __init__(self, person_id=None, name="", email=None):
        self._person_id = person_id
        self._name = name.strip()
        self._email = email

    @property
    def person_id(self):
        return self._person_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value.strip()

    @property
    def email(self):
        return self._email

    @abstractmethod
    def print_details(self):
        pass
