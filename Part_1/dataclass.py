from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    username: str
    email: str
    password: str

    def print_info(self):
        return f"Name: {self.name}\nAge: {self.age}\nUsername: {self.username}\nEmail: {self.email}"


raghav = Person(
    "Raghav Gupta", 19, "raghav-56", "raghav@example.com", "securepassword123"
)
Admin = raghav.print_info()
print(Admin)
print(raghav.password)
