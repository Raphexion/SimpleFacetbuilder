from Person import Person
import unittest


class TestPerson(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pre_built(self):
        p = Person()

        self.assertIs(p.street, None)
        self.assertIs(p.city, None)
        self.assertIs(p.company, None)
        self.assertEqual(p.income, 0)

    def test_address(self):
        street = object()
        city = object()

        p = Person.create().lives() \
            .at(street).city(city) \
            .build()
