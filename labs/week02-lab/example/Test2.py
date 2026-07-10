print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()
print("2. ตัวแปลงเวลา:")
print("   - รับค่าจำนวนวินาทีจากผู้ใช้")
print("   - แปลงเป็นชั่วโมง นาที และวินาทีที่เหลือ")
print("   - ตัวอย่าง: 3661 วินาที = 1 ชั่วโมง 1 นาที 1 วินาที")
print()

# input
second = int(input("second : "))

# process
hours = second // 3600
second_remain = second % 3600

minute = second /60
second_remain = minute * 60

# output
print(f"Hours = {hours}, Minute = {minute}, Second = {second}")