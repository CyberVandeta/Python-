def name_of_function():
    pass


name_of_function()


def add_func(ar1, ar2):
    """It's addition function """
    # it prints the docstring
    print(ar1 + ar2)


add_func(1, 2)


def hello():
    print("hello")


hello()


def greeting(name):
    print("Hello" + name)


greeting(" Kiran")


def add_return(a, b):
    return a + b


x = add_return(3, 4)
print(x)
print(add_return(4, 5))


def is_prime(num):
    """
    Input: A number
    Output: Checks a number is prime oe not
    """
    for n in range(2, num):
        if num % n == 0:
            print("The number is not prime ")
            break  # so the loop breaks we need not to check any more
    else:
        print("The number is prime")


is_prime(15)
is_prime(13)
is_prime(3)
