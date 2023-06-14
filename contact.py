class Contact:
    def __init__(self, name: str, phone: str, comment: str):
        self.name = name
        self.phone = phone
        self.comment = comment

    # Удобный метод для записи контакта в файл
    def to_str(self):
        return f'{self.name}:{self.phone}:{self.comment}'

    def __str__(self):
        return f'{self.name:<20} | {self.phone:<20} | {self.comment:<20}'