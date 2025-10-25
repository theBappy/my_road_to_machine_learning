class shape:
    def draw(self):
        print("draw method")
        return
    
class circle(shape):
    def draw(self):
        print("draw a circle")
        return
    
class circle(shape):
    def draw(self):
        print("draw a circle")
        return
    
class rectangle(shape):
    def draw(self):
        print("draw a rectangle")
        return
    
class area:
    def area(self):
        print("calculated area")
        return
    
def duck_function(obj):
    obj.draw()

objects = [circle(), rectangle(), area()]
for obj in objects:
    duck_function()
