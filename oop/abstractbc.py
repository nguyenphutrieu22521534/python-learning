from abc import ABC, abstractmethod
import math


# Định nghĩa Abstract Base Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        """Tính diện tích hình. Phải được triển khai bởi lớp con."""
        pass

    @abstractmethod
    def perimeter(self):
        """Tính chu vi hình. Phải được triển khai bởi lớp con."""
        pass

    # Có thể có phương thức thông thường (không trừu tượng)
    def description(self):
        return "Đây là một hình học"


# Lớp con triển khai ABC
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle với bán kính {self.radius}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle {self.width}x{self.height}"


# Sử dụng
try:
    shape = Shape()  # Lỗi! Không thể tạo instance từ ABC
except TypeError as e:
    print(f"Lỗi: {e}")

# Tạo các đối tượng từ lớp con
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"{circle}: Diện tích = {circle.area():.2f}, Chu vi = {circle.perimeter():.2f}")
print(f"{rectangle}: Diện tích = {rectangle.area()}, Chu vi = {rectangle.perimeter()}")