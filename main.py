class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, name):
        parts = name.split(" ")
        if len(parts) != 2:
            raise ValueError("Ism va familiya orasida faqat bitta bo'sh joy bo'lishi kerak!")
        self.first_name, self.last_name = parts


p = Person("Ali", "Valiyev")
print(p.full_name)
p.full_name = "Hasan Karimov"
print(p.first_name)
print(p.last_name)
