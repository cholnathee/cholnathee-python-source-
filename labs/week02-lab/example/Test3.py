# เทมเพลตเครื่องคำนวณการซื้อสินค้า

item_price = float(input("ระบุราคาสินค้า: "))
quantity = int(input("ระบุจำนวนสินค้า: "))
discount_percent = float(input("ระบุเปอร์เซ็นต์ส่วนลด: "))
tax_percent = float(input("ระบุเปอร์เซ็นต์ภาษี: "))

# TODO: คำนวณยอดรวมย่อย
subtotal = item_price *quantity

# TODO: คำนวณมูลค่าส่วนลด
discount = subtotal * (discount_percent / 100)

# TODO: คำนวณราคาหลังหักส่วนลด
price = subtotal - discount

# TODO: คำนวณมูลค่าภาษี
tax = price * (tax_percent / 100)

# TODO: คำนวณยอดรวมสุทธิ
final_total = price * tax

# TODO: แสดงรายการในใบเสร็จ
print("Subtotal =", subtotal)
print("Discount =" + str(discount))
print("Tax =",tax)
print("Final total =",final_total)
