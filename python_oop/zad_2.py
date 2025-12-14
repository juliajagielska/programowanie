from typing import List


class Library:
    def __init__(
        self, city: str, street: str, zip_code: str, open_hours: str, phone: str
    ) -> None:
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return (
            f"Biblioteka: {self.city}, {self.street}, {self.zip_code}, "
            f"godziny otwarcia: {self.open_hours}, tel.: {self.phone}"
        )


class Employee:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: str,
        birth_date: str,
        city: str,
        street: str,
        zip_code: str,
        phone: str,
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return (
            f"Pracownik: {self.first_name}, {self.last_name}, "
            f"zatrudniony: {self.hire_date}, ur.: {self.birth_date}, "
            f"adres: {self.city}, {self.street}, {self.zip_code}, "
            f"tel.: {self.phone}"
        )


class Student:
    def __init__(self, name: str, marks: List[int]) -> None:
        self.name = name
        self.marks = marks

    def __str__(self) -> str:
        average = sum(self.marks) / len(self.marks)
        return f"Student: {self.name}, oceny: {self.marks}, " f"średnia: {average:.1f}"


class Book:
    def __init__(
        self,
        library: Library,
        publication_date: str,
        author_name: str,
        author_surname: str,
        number_of_pages: int,
    ) -> None:
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return (
            f"Książka: {self.author_name} {self.author_surname}, "
            f"rok wydania: {self.publication_date}, "
            f"stron {self.number_of_pages}, "
            f"{self.library.city}, {self.library.street}, "
        )


class Order:
    def __init__(
        self, employee: Employee, student: Student, books: List[Book], order_date: str
    ) -> None:
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        books_str = "\n    ".join(str(book) for book in self.books)
        return (
            f"Zamówienie z dnia {self.order_date}\n"
            f"  Pracownik: {self.employee.first_name}, {self.employee.last_name}\n"
            f"  Student: {self.student.name}\n"
            f"  Książki:\n"
            f"    {books_str}"
        )


if __name__ == "__main__":
    library1 = Library(
        city="Warszawa",
        street="Marszałkowska 1",
        zip_code="00-001",
        open_hours="8:00-18:00",
        phone="111-222-333",
    )
    library2 = Library(
        city="Kraków",
        street="Długa 5",
        zip_code="31-001",
        open_hours="9:00-17:00",
        phone="444-555-666",
    )

    employee1 = Employee(
        "Anna",
        "Nowak",
        "2020-01-05",
        "1990-06-10",
        "Warszawa",
        "Marszałkowska 1",
        "00-001",
        "111-222-333",
    )
    employee2 = Employee(
        "Jan",
        "Kowalski",
        "2019-03-10",
        "1985-02-20",
        "Kraków",
        "Długa 5",
        "31-001",
        "444-555-666",
    )
    employee3 = Employee(
        "Ewa",
        "Wiśniewska",
        "2022-09-01",
        "1995-11-30",
        "Warszawa",
        "Marszałkowska 1",
        "00-001",
        "777-888-999",
    )

    student1 = Student("Alicja Król", [80, 75, 90])
    student2 = Student("Piotr Zieliński", [60, 55, 70])
    student3 = Student("Katarzyna Nowak", [40, 50, 45])

    book1 = Book(library1, "2010", "Adam", "Mickiewicz", 320)
    book2 = Book(library1, "2015", "Bolesław", "Prus", 280)
    book3 = Book(library2, "2018", "Henryk", "Sienkiewicz", 450)
    book4 = Book(library2, "2020", "Olga", "Tokarczuk", 380)
    book5 = Book(library1, "2022", "Wisława", "Szymborska", 200)

    order1 = Order(employee1, student1, [book1, book2, book5], "2025-11-24")
    order2 = Order(employee2, student3, [book3, book4], "2025-11-25")

    print(order1)
    print()
    print(order2)
