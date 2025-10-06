# shape.py - Abstraction side of Bridge pattern 

class Shape:
    """Base class for all shapes - defines WHAT to draw"""
    
    def __init__(self, renderer):
        """Initialize shape with a renderer"""
        # This is the bridge - shape uses renderer
        self.renderer = renderer
    
    def draw(self):
        """Draw the shape using the renderer"""
        pass


class Circle(Shape):
    """Circle shape with a specific radius"""
    
    def __init__(self, radius, renderer):
        """Create a circle with given radius and renderer"""
        super().__init__(renderer)
        self.radius = radius
    
    def draw(self):
        """Draw circle by delegating to renderer"""
        # Bridge in action - shape delegates to implementation
        self.renderer.render_circle(self.radius)


class Square(Shape):
    """Square shape with a specific side length"""
    
    def __init__(self, side, renderer):
        """Create a square with given side and renderer"""
        super().__init__(renderer)
        self.side = side
    
    def draw(self):
        """Draw square by delegating to renderer"""
        # Bridge in action - shape delegates to implementation
        self.renderer.render_square(self.side)
