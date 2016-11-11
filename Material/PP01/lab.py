class Dog():
    def bark(self):
        print('dog bark')
class Dog1(Dog):
    def bark(self):
        print('dog1 barkd')

class Dog1(Dog):
    def bark(self):
        print('dog1 bark')
class Husky(Dog1, Dog):
    pass
    # def bark(self):
    #     super(Husky, self).bark()
    #     print('husky woof')
    # def bark(self, pitch=""):
    #     print('husky woof '+pitch)
def main():
    dog = Dog()
    dog.bark()
    husky = Husky()
    husky.bark()
    #husky = (Dog)husky
if __name__ == '__main__':
    main()
