"""
2 types of programming
1) structured programming ==> การเขียนโปรแกรมเชิงโครงสร้าง > c, js python
2) object-oriented programming (OOP) ==> การเขียนโปรแกรมเชิงวัตถุ > java, C#,
python
"""

#วิธีแก้ปัญหา เป็นแค่แนวทาง template แม่แบบ เป็นเหมือนตรายาง
class ClassName:
    """Class docstring"""
    
    # ข้อมูลที่ต้องใช้ในการแก้ไขปัญหา ระบุไว้ใน constructor method
    def __init__(self, parameters):
        # Constructor method
        self.attribute = value
    
    # การกระทำ ==> method
    def method_name(self):
        # Instance method
        return something

    def method_name2(self):
        pass

# การสร้างวัตถุจากคลาส ==> เอาคลาสมาใช้
myObj = ClassName(parameters)

# ใช้งานวัตถุจากคลาส
print(myObj.attribute)
resultFromMethod = myObj.method_name()
myObj.method+name2()

myObj2 = ClassName(parameters)
print(myObj2.attribute)
print(myObj2.method_name())
myObj2.method_name2()