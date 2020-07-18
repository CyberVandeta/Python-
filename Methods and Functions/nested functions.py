#Enclosing function local
def greet():
    name = "Kiran"

    def hello():
        print('Hello', name)

    hello()


greet()
