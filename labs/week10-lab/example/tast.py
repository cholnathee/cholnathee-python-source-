#1. รับค่า text จากผู้ใช้
#2. รับค่าอักขระที่ต้องการค้นหาจากผู้ใช้
#3. แสดงผลจำนวนอักขระในข้อความ text

# ตัวอย่างหน้าจอ
# Insert your text in: Boonchoo Hitnupuoug
# Character to find: o
# 5 letters 'o' found in 'Boonchoo Hitnupuoug'

print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("กรอกชื่อ:")
char = input("Character to find: ")
for letter in text:
    if letter == char:
        count += 1
print(f"{count} letters '{char}' found in '{text}'")

# เขียนโปรแกรมตรวจสอบความแข็งแรงของ PASSWORD
# นิยามของ strong password คือ ยาวมากกว่า 8 ตัว, มีอักขระ @ 1 ตัว, มีตัวเลข, มีตัวอักษร
#
# ตัวอย่างหน้าจอ
# Insert your password: Boonchoo
# Your password is not strong!
#
# Insert your password: Test@123
# Your password is strong

"""
test_str = input('กรอกรหัสผ่าน:')
print(f"\nValidation methods for '{test_str}':")
print(f"isalnum(): {test_str.isalnum()}")
print(f"isalpha(): {test_str.isalpha()}")
print(f"isdigit(): {test_str.isdigit()}")
print(f"isupper(): {test_str.isupper()}")
print(f"islower(): {test_str.islower()}")
"""
password = input("Insert your password: ")
lenght = len(password)
words = password.split('@')

if len(words) > 1 and password.count('@') == 1:
    left = words[0].isalnum()
    right = words[1].isalnum()
else:
    left = False;
    right = False;

if lenght >= 8 and len(words) == 2 and left == True and right == True:
    print("Your password is strong!")
else:
    print("Your password is not strong!")

"""
password = input("Insert your password: ")

has_at = '@' in password
has_digit = any(char.isdigit() for char in password)
has_alpha = any(char.isalpha() for char in password)
is_long_enough = len(password) > 8

if has_at and has_digit and has_alpha and is_long_enough:
    print("Your password is strong")
else:
    print("Your password is not strong!")
"""