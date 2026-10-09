"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

เขียนคลาส Python ชื่อ Rectangle โดยมีรายละเอียดดังนี้:

มีแอตทริบิวต์แบบ private สำหรับเก็บค่าความยาวและความกว้าง
มีเมธอดสำหรับคำนวณพื้นที่ (getArea()) และเส้นรอบรูป (getPerimeter())
มีเมธอดสำหรับตรวจสอบว่าเป็นรูปสี่เหลี่ยมจัตุรัสหรือไม่ (isSquare())

"""

class Rectangle:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def getArea(self):
        return f"Area of {self.__width} width and {self.__length} length = {self.__width * self.__length}"

    def getPerimeter(self):
        return f"Perimeter of {self.__width} width and {self.__length} length = {2 * (self.__width + self.__length)}"

    def isSquare(self):
        return self.__width == self.__length


my_rectangle = Rectangle(5, 10)

print(my_rectangle.getArea())
print(my_rectangle.getPerimeter())
print(f"Is square: {my_rectangle.isSquare()}")
    