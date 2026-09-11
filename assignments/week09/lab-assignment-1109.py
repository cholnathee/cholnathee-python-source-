"""
เครื่องคำนวณค่าไฟแบบขั้นบันได
เขียนโปรแกรมคำนวณค่าไฟฟ้าจากจำนวนหน่วยไฟฟ้าที่ใช้ในเดือนนั้น โดยใช้ฟังชั่น
calculate_electricity_cost(units)

ค่าไฟฟ้าขึ้นกับปริมาณการใช้งาน
จำนวนหน่วยที่ใช้     อัตราต่อหน่วย
1-50 หน่วย           2.50 บาท
51-100 หน่วย         3.00 บาท
101-200 หน่วย        3.50 บาท
มากกว่า 200 หน่วย      4.00 บาท
"""
"""
units = 120
cost = (2.50 * 50) + (3.00 * 50) + (3.50 * 50) + (4.00 * 50) + 25
print(units,cost)
"""

def calculate_electricity_cost(units):
    print("\nรายละเอียดค่าไฟ:")

    if units <= 50:
        cost1 = units * 2.50
        print(f"1-{units} หน่วย: {cost1} บาท")
        total_units_cost = cost1

    elif units <= 100:
        cost1 = 50 * 2.50
        cost2 = (units - 50) * 3.00
        print(f"1-50 หน่วย: {cost1} บาท")
        print(f"51-{units} หน่วย: {cost2} บาท")
        total_units_cost = cost1 + cost2

    elif units <= 200:
        cost1 = 50 * 2.50
        cost2 = 50 * 3.00
        cost3 = (units - 100) * 3.50
        print(f"1-50 หน่วย: {cost1} บาท")
        print(f"51-100 หน่วย: {cost2} บาท")
        print(f"101-{units} หน่วย: {cost3} บาท")
        total_units_cost = cost1 + cost2 + cost3

    else:
        cost1 = 50 * 2.50
        cost2 = 50 * 3.00
        cost3 = 100 * 3.50
        cost4 = (units - 200) * 4.00
        print(f"1-50 หน่วย: {cost1} บาท")
        print(f"51-100 หน่วย: {cost2} บาท")
        print(f"101-200 หน่วย: {cost3} บาท")
        print(f"201-{units} หน่วย: {cost4} บาท")
        total_units_cost = cost1 + cost2 + cost3 + cost4

    service_fee = 25.00
    total = total_units_cost + service_fee
    print(f"ค่าบริการ: {service_fee} บาท")
    print(f"รวมค่าไฟทั้งสิ้น: {total} บาท")

    return total


def main():
    while True:
        print("\n==== โปรแกรมคำนวณค่าไฟฟ้า ====")
        print("1. คำนวณค่าไฟ")
        print("2. ออกจากโปรแกรม")
        choice = input("เลือกเมนู: ")

        if choice == "1":
            units = int(input("\nกรอกจำนวนหน่วยไฟฟ้า: "))
            if units < 0:
                print("จำนวนหน่วยไฟฟ้าต้องไม่ติดลบ")
            else:
                calculate_electricity_cost(units)

        elif choice == "2":
            print("ออกจากโปรแกรม...")
            break

        else:
            print("เลือกเมนูไม่ถูกต้อง")


main()