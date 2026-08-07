"""
Assignment 2.1: โปรแกรมเพื่อการตรวจสอบผลการสอบ (exam-score.py)

ให้รับคะแนนสอบของนักเรียนจำนวน 5 คนเก็บไว้ในตัวแปรชนิด list จากนั้นให้ตรวจสอบคะแนนของนักเรียนแต่ละคนว่าผ่านหรือไม่ผ่าน โดยกำหนดว่าคะแนน 50 คะแนนขึ้นไปถือว่าผ่าน

กระบวนการทำงาน
รับคะแนน 5 ค่า เก็บคะแนนทั้งหมดไว้ใน list (เก็บคะแนนทั้งหมดก่อนค่อยไปตรวจสอบ)
ใช้ loop ตรวจสอบคะแนนทีละค่า (ใช้ "for" loop วน เพื่อการตรวจสอบ)
ใช้ condition (if-else) แสดงผลว่า “ผ่าน” หรือ “ไม่ผ่าน”
"""

"""
(รุ่นแรก)
score = input("Enter score of student 1:")
score1 = input("Enter score of student 2:")
score2 = input("Enter score of student 3:")
score3 = input("Enter score of student 4:")
score4 = input("Enter score of student 5:")
scores = ({score},{score1},{score2},{score3},{score4})
for :
    score >= 50
    print("Student 1: {score} -> ผ่าน")
"""
scores = []
# 1. รับคะแนน 5 ค่า แปลงเป็นตัวเลข และเก็บไว้ใน list
for i in range(1, 6):
    score = int(input(f"Enter score of student {i}: "))
    scores.append(score)

# 2. ใช้ for loop ตรวจสอบคะแนนทีละค่า
# enumerate(..., 1) ช่วยให้ได้ลำดับนักเรียนเริ่มจาก 1 ถึง 5
for index, score in enumerate(scores, 1):
    # 3. ใช้ condition (if-else) แสดงผล Pass/Fail
    if score >= 50:
        print(f"Student {index}: {score} -> ผ่าน")
    else:
        print(f"Student {index}: {score} -> ไม่ผ่าน")