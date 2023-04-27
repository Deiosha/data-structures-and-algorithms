from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        # creating an empty list for dogs and cats
        self.cats = []
        self.dogs = []

    #  takes one parameter called "animal",  instance of Dog or Cat class
    #  purpose: add the animal instance to a list of dogs or cats
    def enqueue(self, animal):
        # check to see if its instance of cat
        if isinstance(animal, Cat):
            # appending animal to cats
            self.cats.append(animal)
            # check to see if its instance of dog
        elif isinstance(animal, Dog):
            # appending animal to dogs
            self.dogs.append(animal)

    def dequeue(self, animal_type):
        # taking in a string, self,cats list
        if animal_type == "cat" and self.cats:
            # removes the first cat from list using pop
            return self.cats.pop(0)
        # dog and list self.dogs is not empty,
        # removes and returns the first dog object from the self.dogs list using the pop() method.
        elif animal_type == "dog" and self.dogs:
            return self.dogs.pop(0)
        else:
            # anything other than cat or dog returns None.
            return None


class Dog:
    pass


class Cat:
    pass
