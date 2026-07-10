print("Now try these exercises:")
print()
print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print()
print("ลองทำแบบฝึกหัดเหล่านี้ดู:")
print()
print("1. โปรแกรมคำนวณเกี่ยวกับวงกลม:")
print("   - รับค่ารัศมีจากผู้ใช้")
print("   - คำนวณพื้นที่ (π * r²)")
print("   - คำนวณเส้นรอบวง (2 * π * r)")
print("   - ใช้ค่า 3.14159 สำหรับ π")
print()

#input
radius = float(input("radius:"))

#procass
area = 3.14159 * radius ** 2
circumference = 2 * 3.14159 * radius

#output
print("area :",area)
print("circmference :",circumference)
print(f"Area = {area}, circmference = {circumference}")