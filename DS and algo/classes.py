class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self,color):
        self.color = color
    


cookie_one = Cookie("green")
cookie_two = Cookie("blue")

print(f"we have a {cookie_one.get_color()} cookie")
print(f"we have a {cookie_two.get_color()} cookie")

cookie_one.set_color("yellow")
print(f"we changed the color with {cookie_one.get_color()}")