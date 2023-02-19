class Person:
    name = "Alice"
    age = "30"
    gender = "female"

    def set(self, name, age, gender):
        # print(self.name)
        # print(self.age)
        # print(self.gender)
        self.name = name
        self.age = age
        self.gender = gender

    def get(self, name, age, gender):
        print("My name is {}".format(self.name))
        print("My age is {}".format(self.age))
        print("My gender is {}".format(self.gender))

    def info(self):
        print("Name: [" + self.name + "],", "Age: [" + self.age + "],", "Gender: [" + self.gender + "]")

    def voter_check(self):
        pass


person = Person()
person.info()


class Voter(Person):

    voter = "voter"

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_gender(self, gender):
        self.gender = gender

    def get(self, name, age, gender):
        print("My name is {}".format(self.name))
        print("My age is {}".format(self.age))
        print("My gender is {}".format(self.gender))

    def voter_check(self):
        age = self.age

        try:
            print(self.age + " ,the person is able to vote")
        except:
            print("An error occurred, check if a number was given")
        if age < 18:
            raise TypeError(self.age + " ,the person is too young to vote")

    def print_info(self):
        print("My name is {}".format(self.name))
        print("My age is {}".format(self.age))
        print("My gender is {}".format(self.gender))


person = Voter()
person.set_name("John")
person.set_age("20")
person.set_gender("female")
person.print_info()
person.voter_check()
