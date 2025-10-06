# renderer.py - Implementation side of Bridge pattern

class Renderer:
    """Base class for all renderers - defines HOW to draw shapes"""
    
    def render_circle(self, radius):
        """Render a circle with given radius"""
        pass
    
    def render_square(self, side):
        """Render a square with given side length"""
        pass


class VectorRenderer(Renderer):
    """Renders shapes using vector graphics (lines and curves)"""
    
    def render_circle(self, radius):
        # Draw circle using vectors
        print(f"Drawing a circle of radius {radius} with vectors")
    
    def render_square(self, side):
        # Draw square using vectors
        print(f"Drawing a square with side {side} using vectors")


class RasterRenderer(Renderer):
    """Renders shapes using raster graphics (pixels)"""
    
    def render_circle(self, radius):
        # Draw circle using pixels
        print(f"Drawing a circle of radius {radius} with pixels")
    
    def render_square(self, side):
        # Draw square using pixels
        print(f"Drawing a square with side {side} using pixels")
