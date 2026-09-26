def deposit(money):
    balance = 1000
    try:
        amount = float(money)
        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
    except ValueError as e:
        print(f"เกิดข้อผิดพลาด: {e}")
    else:
        balance += amount
        print("ฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {balance:.2f} บาท")
    finally:
        print("สิ้นสุดรายการฝากเงิน")


# ทดลองใช้งาน function
print("ยอดเงินเริ่มต้น: 1000 บาท")
money = input("กรอกจำนวนเงินที่ต้องการฝาก: ")
deposit(money)