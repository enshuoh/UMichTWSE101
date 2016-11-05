class Dog():
    def bark(self):
        print('dog bark')

class Husky(Dog):
    # def bark(self):
    #     # super(Husky, self).bark()
    #     print('husky woof')
    def bark(self, pitch=""):
        print('husky woof '+pitch)
def main():
    dog = Dog()
    dog.bark()
    husky = Husky()
    husky.bark()
    #husky = (Dog)husky
if __name__ == '__main__':
    main()
