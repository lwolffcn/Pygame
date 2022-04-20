import sys

class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaah ...')
            self.hungry = False
        else:
            print('No, thanks!')

    def sing(self):
        print("Maybe not super().sing()")


class SongBird(Bird):
    def __init__(self):
        #Bird.__init__(self)
        super().__init__()
        self.sound = 'Squawk!'
    def sing(self):
        #super().sing()
        print(self.sound)

sb = SongBird()
#Bird.__init__(sb)
sb.sing()
sb.eat()
sb.eat()

