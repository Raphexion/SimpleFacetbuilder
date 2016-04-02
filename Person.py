class Person:
    def __init__(self):
        self.street = None
        self.city = None
        self.company = None
        self.income = 0

    @staticmethod
    def create():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def lives(self):
        return PersonAddressBuilder(self.person)

    def works(self):
        return PersonEmploymentBuilder(self.person)

    def build(self):
        return self.person


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__()
        self.person = person

    def at(self, street):
        self.person.street = street
        return self

    def city(self, city):
        self.person.city = city
        return self

    def code(self, code):
        self.person.code = code
        return self


class PersonEmploymentBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__()
        self.person = person

    def at(self, company):
        self.person.company = company
        return self

    def income(self, income):
        self.person.income = income
        return self
