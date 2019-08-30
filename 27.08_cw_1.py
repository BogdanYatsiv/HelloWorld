class Figure:
    color = None

    def __init__(self,new_color):
        self.color = new_color

    def get_color(self):
        return self.color

    def info(self):
        print(f"Figure with {self.color} color")

class Square(Figure):
    side = None

    def __init__(self,new_color, new_side):
        super().__init__(new_color)
        self.side = new_side

    def square(self):
        return self.side**2

    def info(self):
        print(f"Square with {self.color} color and side {self.side}")

class Rectangle(Figure):
    height = None
    width = None

    def __init__(self,new_color,new_height,new_width):
        super().__init__(new_color)
        self.height = new_height
        self.width = new_width

    def square(self):
        return self.height*self.width

    def info(self):
        print(f"Rectangle with {self.color} color and height {self.height}, width {self.width}")