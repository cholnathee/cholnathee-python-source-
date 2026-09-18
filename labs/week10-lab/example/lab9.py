"""
โจทย์ 1: เครื่องคำนวณอย่างปลอดภัย
เขียนโปรแกรมรับตัวเลข 2 จำนวนและตัวดำเนินการ 1 ตัว ได้แก่ + - * / แล้วแสดงผลลัพธ์
โปรแกรมต้องจัดการกรณีต่อไปนี้
  • ผู้ใช้กรอกข้อมูลที่ไม่ใช่ตัวเลข #ValueError
  • ผู้ใช้เลือกตัวดำเนินการอื่นนอกเหนือจาก + - * / raise ValueError
  • ผู้ใช้พยายามหารด้วยศูนย์ #ZeroDivisionError
  • โปรแกรมต้องแสดง จบการทำงาน เสมอด้วย finally

ตัวอย่างผลลัพธ์ที่คาดหวัง

ตัวเลขที่ 1: 10
ตัวเลขที่ 2: 0
เครื่องหมาย (+, -, *, /): /

ไม่สามารถหารด้วยศูนย์ได้
จบการทำงาน
"""
try:
    num1 = float(input("ตัวเลขที่ 1: "))
    num2 = float(input("ตัวเลขที่ 2: "))
    operator = input("เครื่องหมาย (+, -, *, /): ")

    if operator not in ['+', '-', '*', '/']:
        raise ValueError("เครื่องหมายไม่ถูกต้อง")

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        # หาก num2 เป็น 0 บรรทัดนี้จะเกิด ZeroDivisionError อัตโนมัติ
        result = num1 / num2
        
except ValueError as error:
    print(f"ข้อมูลไม่ถูกต้อง กรุณากรอกตัวเลขและเครื่องหมายที่กำหนด")

except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")

else:
    print(f"ผลลัพธ์: {result}")

finally:
    print("จบการทำงาน")