def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

# print(add(1, 2, 3, 4, 5))

def calculate(n, **kwargs):
    # print(type(kwargs))
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)

# calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")  # better than
# kwargs["make"] bc in case it doesn't exist -> returns None
        self.model = kwargs.get("model")


my_car = Car(make="Nissan")
print(my_car.model)