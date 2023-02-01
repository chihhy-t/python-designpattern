from abc import ABCMeta, abstractmethod

# Interface
class Shape(metaclass=ABCMeta):
  @abstractmethod
  def area(self):
    raise NotImplementedError()

class Rectangle(Shape):
	def __init__(self, width, height):
		self.width = width
		self.height = height
	def area(self) -> float:
		return self.width * self.height

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius
	def area(self) -> float:
		return self.radius * self.radius * 3.14

class main():
  rectangle = Rectangle(10, 2)
  print(rectangle.area())
  circle = Circle(5)
  print(circle.area())

if __name__ == '__main__':
	main()