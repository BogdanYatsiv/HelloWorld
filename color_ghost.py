from random import choice

class Ghost:
    color: str

    def __init__(self):
        self.color = choice(["white","yellow","purple","red"])