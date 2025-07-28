class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def move(self, direction):
        print(f"{self.name} moves {direction}.")

    def shoot(self):
        print(f"{self.name} shoots!")