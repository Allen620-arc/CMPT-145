class Hero(object):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def say_hello(self):
        print('Hello, evil-doers! My name is', self.name + '!')
        print('My super power is', self.power, 'so you better beware.')



bruce = Hero('Batman', 'martial arts')
bruce.say_hello()

diana = Hero('Wonder Woman', 'super strength')
diana.say_hello()



