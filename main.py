# main.py - Demo Application

from renderer import VectorRenderer, RasterRenderer
from shape import Circle, Square


def main():
    """Main function demonstrating the Bridge pattern"""
    
    # Create renderers (implementation objects)
    vector = VectorRenderer()
    raster = RasterRenderer()
    
    print("=== Bridge Pattern Demo ===\n")
    
    # Circle with Vector Renderer
    print("Circle with Vector Renderer:")
    circle1 = Circle(5, vector)
    circle1.draw()
    
    # Circle with Raster Renderer - same shape, different renderer
    print("\nCircle with Raster Renderer:")
    circle2 = Circle(7, raster)
    circle2.draw()
    
    # Square with Vector Renderer
    print("\nSquare with Vector Renderer:")
    square1 = Square(10, vector)
    square1.draw()
    
    # Square with Raster Renderer - same shape, different renderer
    print("\nSquare with Raster Renderer:")
    square2 = Square(15, raster)
    square2.draw()
    
    print("\n=== Demo Complete ===")
    # Bridge pattern allows mixing 2 shapes with 2 renderers = 4 combinations
    # without creating 4 separate classes


if __name__ == "__main__":
    main()
