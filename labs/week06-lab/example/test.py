def greet_person(name):
    """Greets a person by name"""
    print(f"Hello, {name}! Nice to meet you.")

print("Calling greet_person with different names:")
greet_person(5)
greet_person("Bob")
greet_person("Charlie")
print()

"""
เขียน Function แปลงหน่วยสกุลเงิน ที่สามารถแปลงเงินจาก
THB <-> USD ..1 USD = 32 THB

โดยใช้ชือและการใช้งาน
function convart_Currency(100,"USD")

แสดงผลออกทางหน้าจอ
100 THB = 3.3 USD
"""

def convart_Currency(currency, title):
    rate = 32
    if title == "USD":
        sum = currency * rate
        print(f"{currency} {title} = {sum} THB ")
    else:
        sum = currency / rate
        print(f"{currency} {title} = {sum} USD ")


convart_Currency(100,"USD")
convart_Currency(100,"THB")