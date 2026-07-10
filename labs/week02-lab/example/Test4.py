print("4. BMI Calculator:")
print("   - Ask for weight (kg) and height (m)")
print("   - Calculate: BMI = weight / (height ** 2)")
print()
print("4. โปรแกรมคำนวณค่า BMI:")
print("   - รับค่าน้ำหนัก (กก.) และส่วนสูง (ม.)")
print("   - คำนวณ: BMI = น้ำหนัก / (ส่วนสูง ** 2)")
print()

# input
kg = float(input("ใส่น้ำหนัก :"))
cm = float(input("ใส่ส่วนสูง :"))

# process
bmi = kg / (cm ** 2)

# output
print("ค่า BMI คือ",bmi)