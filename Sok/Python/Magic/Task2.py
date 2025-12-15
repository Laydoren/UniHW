class User:
    @staticmethod
    def _validate_name(name):
        if not isinstance(name, str) or not name.isalpha():
            raise ValueError("Err name")
        return name

    @staticmethod
    def _validate_age(age):
        if not isinstance(age, int) or not (0 <= age <= 110):
            raise ValueError("Err age")
        return age

    def __init__(self, name, age):
        self.__name = User._validate_name(name)
        self._age = User._validate_age(age)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = User._validate_name(new_name)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = User._validate_age(new_age)


try:
    u = User("Bob", 17)
    print(f"User= {u.name}, Age= {u.age}")

    u.name = "ObO"
    u.age = 87
    print(f"Name= {u.name}, Age= {u.age}")

except ValueError as e:
    print(f"Error: {e}")
