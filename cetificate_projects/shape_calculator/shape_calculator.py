class Rectangle:
    def __init__(self, width,height):
        self.width = width
        self.height = height

    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, rect):
        return (self.width // rect.width) * (self.height // rect.height)

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)

class Square(Rectangle):
    def __init__(self, width):
        super().__init__(self, width, width)

    def set_side(self, side):
        super().set_height(self, side)
        super().set_width(self, side)
    
    def set_width(self, side):
        self.set_side(side)
    
    def set_height(self, side):
        self.set_side(side)
    
    def __str__(self):
        return "Square(side={})".format(self.width)