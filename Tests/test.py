class Robot():
    """A Robot class"""
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    
    def introduce_self(self):
        print("My name is " + self.name)


    
r1 = Robot("Jorge", "Verde", 30)
r1.introduce_self()

r2 = Robot("Lucas", "Verde", 30)
r2.introduce_self()