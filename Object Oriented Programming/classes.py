class Dog():
    spesies = 'mammal'

    def __init__(self, breed, name, fur=True):
        self.breed = breed
        self.name = name
        self.fur = fur


sam = Dog(breed='Lab', name='sammy', fur=False)
print(sam.breed)
print(sam.name)
print(sam.spesies)
print(sam.fur)
