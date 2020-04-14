class GotCharacter:
    def __init__(self, first_name=None, is_alive=True):
        self.firt_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """A class representing the Stark House from GoT"""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = 'Stark'
        self.house_words = 'Winter is Coming'

    def die(self):
        self.is_alive = False

    def print_house_words(self):
        print(self.house_words)


class Lannister(GotCharacter):
    """A class representing the Lannister House from GoT"""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.house_words = 'Hear me Roar!'

    def die(self):
        self.is_alive = False

    def print_house_words(self):
        print(self.house_words)
