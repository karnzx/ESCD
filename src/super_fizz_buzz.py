"""
SOLID Principles

SRP (Single Responsibility Principle)
only one job.
FizzBuzz only return Fizz Buzz word up to provided number

OCP (Open-Closed Principle)
Making new inherit's FizzBuzz class with new or additonal of fizzbuzz conditions
there no need to edit parent class

"""


class FizzBuzz:
    def __init__(self, number: int) -> None:
        self.number = number

    def fizz(self):
        if self.number % 3 == 0:
            return "Fizz"
        return ""

    def buzz(self):
        if self.number % 5 == 0:
            return "Buzz"
        return ""

    def get_fizz_buzz(self):
        result = ""
        result += self.fizz()
        result += self.buzz()
        if not result:
            result = "NoFizzBuzz"
        return result


class SuperFizzBuzz(FizzBuzz):
    def __init__(self, number: int) -> None:
        super().__init__(number)

    def fizz(self):
        if self.number % 9 == 0:
            return "FizzFizz"
        return super().fizz()

    def buzz(self):
        if self.number % 25 == 0:
            return "BuzzBuzz"
        return super().buzz()
