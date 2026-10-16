"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

เขียนโปรแกรมเพื่อวิเคราะห์อุณหภูมิรายวันตลอดระยะเวลาหนึ่งสัปดาห์ โดยมีรายละเอียดดังนี้:

สร้างฟังก์ชัน `get_temperatures()` ซึ่งทำหน้าที่:

- ใช้รายการ (list) ภายในฟังก์ชันเพื่อเก็บค่าอุณหภูมิ 7 ค่า (สามารถรับค่าผ่านการป้อนข้อมูลหรือกำหนดค่าไว้ล่วงหน้าก็ได้)
- ส่งคืนรายการดังกล่าว

สร้างฟังก์ชัน `analyze_temps(temp_list)` ซึ่งทำหน้าที่:

- คำนวณและส่งคืนค่าอุณหภูมิเฉลี่ย (โดยใช้ตัวแปรภายในฟังก์ชัน)
- หาและส่งคืนค่าอุณหภูมิสูงสุด
- หาและส่งคืนค่าอุณหภูมิต่ำสุด
- ส่งคืนค่าทั้งสามรายการในรูปแบบทูเพิล (tuple)

สร้างฟังก์ชัน `display_analysis(avg, high, low)` ซึ่งทำหน้าที่แสดงผลลัพธ์ออกมาในรูปแบบที่อ่านง่าย

ตัวอย่างผลลัพธ์:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""

class i:

    def get_temperatures():
        temps = [31 , 30, 20, 24, 22, 32, 40]
        return temps

    def analyze_temps(temp_list):

        average = sum(temp_list) / 7
        high = max(temp_list)
        low = min(temp_list)

        """
        for i in range(7):
            sum += temp_list[i]

            if temp_list[i] > max:
                max = temp_list[i]
        """

        return (average, high, low)

    def display_analysis(avg, high, low):
        print("Temperature Analysis for the Week:")
        print("Average: %.1f C" %avg)
        print("Highest: %.1f C" %high)
        print("Lowest: %.1f C" %low)

temps = i.get_temperatures()
print(temps)
result = i.analyze_temps(temps)
print(result)
i.display_analysis(result[0], result[1], result[2])
        
        
