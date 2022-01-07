from math import pi


def main():
    # variable

    # integer = 1  # int
    # string = "hello"  # str
    # float_ = 0.1
    # bool_ = False  # True
    # tuple_ = (0, 1, "23", False)
    # list_ = [1, 2, 0.5, False, "4"]

    integer: int = 1  # int
    string: str = "hello"  # str
    float_: float = 0.1
    bool_: bool = False  # True
    tuple_: tuple = (0, 1, "23", False)
    list_: list = [1, 2, 0.5, False, "4"]

    print(type(integer), "integer")
    print(type(string), "string")
    print(type(float_), "float_")
    print(type(bool_), "bool_")
    print(type(tuple_), "tuple_")
    print(type(list_), "list_")


    # logic operators

    # False = 0
    # True = 1
    print(not True)  # -> False
    print(not False)  # -> True
    print(False and False)  # -> False
    print(False & False)  # -> False

    print(False or False)  # -> False
    print(False | False)  # -> False

    print(False and True)  # -> False
    print(False & True)  # -> False

    print(False or True)  # -> True
    print(False | True)  # -> True

    print(True and True)  # -> True
    print(True & True)  # -> True

    print(True or True)  # -> True
    print(True | True)  # -> True

    print(not True or not True)  # -> False

    # comparison

    print(1 > 1)  # ->False
    print(1 >= 1)  # ->True
    print(1 <= 1)  # ->True
    print(1 <= 1)  # ->True
    print(1 != 1)  # ->False
    print(1 != 0)  # ->True

    if 5 > 2:
        print("Five is greater than two!")

    i = 1

    while i <= 10:  # True:
        print(f" {i} % 2 = {i % 2}")
        # print(f" {i} % 5 = {i % 5}")
        # print(f" 5 % {i} = {5 % i}")

        # print(f" {i} & 2 = {i & 2}")
        # print(f" {i} & 5 = {i & 5}")
        # print(f" 5 & {i} = {5 & i}")
        i += 1

    print(f"{integer+1=} {integer-1=} {integer*1=} {integer/1=}")
    # print(f"{integer.__add__(1)=} {integer.__sub__(1)=} {integer.__mul__(1)=} {integer.__divmod__(1)=}")

    print(f"{string.lower()=} {string.upper()=} {string.isupper()=}")

    print(f"{tuple_.count(1)=} {tuple_.count(0)=}")

    print(f"{list_[1]=}")

    function("a")  # -> functions arg: a
    function_("a", "b")  # -> functions args: ('a', 'b')
    function__(a="a", b="b")  # -> functions args: {'a': 'a', 'b': 'b'}
    function_ab(1, 2)  # -> functions a: {1}, b {2}
    function_ab(1, "2")  # -> functions a: {1}, b {2}
    # function("a", "b") # -> TypeError: function() takes 1 positional argument but 2 were given
    # function_("a", b="b")  # -> TypeError: function_() got an unexpected keyword argument 'b'
    # function__("a","b")  # ->TypeError: function__() takes 0 positional arguments but 2 were given

    # https://www.w3schools.com/python/


def function(arg):
    print(f"functions arg: {arg}")


def function_ab(a: int, b: int):
    print(f"functions a: {a}, b {b}")


def function_(*args):
    print(f"functions args: {args}")


def function__(**kwargs):
    print(f"functions kwargs: {kwargs}")


def d(r):
    return r * 2


class Circle:
    r = 4

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def d(self):
        return d(self.r)

    def set_r(self, r):
        self.r = r


class MyClass(Circle):

    def __init__(self, name, x, y):
        super().__init__(name, x, y)

    def a(self):
        return (pi * self.r) ** 2  # ADD build in function


if __name__ == '__main__':
    print("Hello, World!")
    print("Universe!")

    main()
"""
    k = 2  # Circle
    kx = 2  #
    ky = 0  #

    print(f"diameter : {k*2}")  # -> diameter : 4
    # ...

    circle = Circle("c1", 2, 0)
    print(f"diameter : {circle.d()}")  # -> diameter : 8

    my_class = MyClass("c1", 2, 0)
    my_class.set_r(5)
    print(f"aria : {my_class.a()}")  # -> aria : 246.74011002723395
"""
