"""
คำถามที่ 2: โปรแกรมแปลงสกุลเงิน (20 คะแนน)

เขียนโปรแกรมเพื่อแปลงค่าเงินระหว่างเงินบาทไทย (THB) และดอลลาร์สหรัฐ (USD)
ข้อกำหนด:

ให้ผู้ใช้เลือกว่าต้องการแปลงค่าเงินในทิศทางใด (THB เป็น USD หรือ USD เป็น THB)
รับค่าจำนวนเงินที่ต้องการแปลง
ใช้อัตราแลกเปลี่ยน: 1 USD = 35.5 THB
แสดงผลลัพธ์โดยกำหนดทศนิยม 2 ตำแหน่ง
แสดงสูตรคำนวณที่ใช้
"""

print("1.THB to USD")
print("2.USD to THB")

rate = 35.5

while True:
    try:    
        choice = input("กรอกสกุลเงิน 1หรือ2 :")
    
        if choice not in ["1","2"]:
            print("กรุณาเลือกเฉพาะเมนู 1 หรือ 2 เท่านั้น")
            continue

        amount = float(input("กรอกจำนวนเงิน :"))

        if amount < 0:
            print("จำนวนเงินต้องไม่ติดลบ")
            continue
        break
    except ValueError:
        print("กรุณากรอกจำนวนเงินเป็นตัวเลขเท่านั้น")

print("\n--- ผลลัพธ์การคำนวณ ---")
if choice == "1":
    result = amount / rate
    print(f"สูตรคำนวณ : {amount:.2f} THB / {rate} = {result:.2f} USD")
    print(f"ผลลัพธ์ : {result:.2f} USD")
elif choice == "2":
    result = amount * rate
    print(f"สูตรคำนวณ : {amount:.2f} USD * {rate} = {result:.2f} THB")
    print(f"ผลลัพธ์ : {result:.2f} THB") 

print("อัตราแลกเปลี่ยนที่ใช้ 1 USD = 35.5 THB")