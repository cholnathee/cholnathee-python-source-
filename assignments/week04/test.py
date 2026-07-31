# รับชื่อจริง (หรือข้อความ) จากผู้ใช้
# รับจำนวนสระทั้งหมดในข้อความขึ้นว่ามีกี่ตัว (a,e,i,o,u)

#ตัวอย่างหน้าจอ
# What is your name? : Boonchoo
# Your test have 4 vowels

name = input("What is your name? :")
"""name1 = list(name)
print(name1)


a = letters.count("a")
e = letters.count("e")
i = letters.count("i")
o = letters.count("o")
u = letters.count("u")

A = letters.count("A")
E = letters.count("E")
I = letters.count("I")
O = letters.count("O")
U = letters.count("U")

count = a + e + i + o + u
"""

#Andy

count = 0
for letter in name:
    if letter == 'a' or letter == 'A':
        count = count + 1
    if letter == 'e' or letter == 'E':
        count = count + 1
    if letter == 'i' or letter == 'I':
        count = count + 1
    if letter == 'o' or letter == 'O':
        count = count + 1
    if letter == 'u' or letter == 'U':
        count = count + 1

count = 0
for letter in name:
    if letter in ['a','e','i','o','u','A','E','I','O','U']:
        count = count + 1

    #print("ตัวอักษร: {letter}")
#print("Your text have",count,"vowels")