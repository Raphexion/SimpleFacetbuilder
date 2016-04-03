# SimpleFacetbuilder

Imagine that you have a class that is composed of
fields from different sub-categories. In this example
we are going to work with a Person class.

In this simple example we have 2 sub-categories with two fields in each:

* Address
  * Street name
  * City
* Employment
  * Company
  * Income

We could initialize the four fields (Street, City, Company and Income),
directly like this (which is perfectly fine in such a small example).

    p = Person(street, city, company, income)

Keep in mind that this is a simplified example to show the pattern.

Instead of constructing the Person object directly we are going to use
2 different builders to do it.

One way of thinking is that we will:

* create the object with default fields
* pass around a reference (pointer) to this object
* different *builders* will provide an *API* to fill in some of the fields
* finally we will extract/pass the object

        p = Person.create() \
            .lives() \
            .at('10 Downing Street').city('London') \
            .works() \
            .at('The British Government').income(100) \
            .build()


## How to test

$ nosetests3
