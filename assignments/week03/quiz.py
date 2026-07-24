# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:

if age >= 0  and age <= 12  :
    print("Child")
if age >= 13 and age <= 19  :
    print("Teenager")
if age >= 20 and age <= 59 :
    print("Adult")
if age > 60 :
    print("Senior")

# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("กรอกรหัส :")
    while True:
        print("\n1. จำนวนเงินคงเหลือ")
        print("2. ถอน")
        print("3. ฝาก") 
        print("4. ออก")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice == "1":
            print("เงินคงเหลือ : ",balance)
        if choice == "2":
            amount = int(input("กรองจำนวนเงินที่ต้องการถอน: "))
            if amount <= 0:
                print("จำนวนเงินที่ถอนต้องมากกว่า 0")
            elif amount > balance:
                print("เงินในบัญชีไม่เพียงพอ")
            else:
                balance -= amount
                print("ถอนเงินสำเร็จ ยอดคงเหลือ:", balance)
        if choice == "3":
            amount = int(input("กรองจำนวนเงินที่ต้องการฝาก: "))
            if amount <= 0:
                print("จำนวนเงินฝากต้องมากกว่า 0")
            else:
                balance += amount
                print("ฝากเงินสำเร็จ ยอดคงเหลือ:", balance)
        if choice == "4":
            break
        
else:
    print("รหัสผิด")
