"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""

print("=== PERSONAL INFORMATION VALIDATOR ===")

name = input("Enter your name: ").strip()
age_str = input("Enter your age: ").strip()
phone = input("Enter your phone number: ").strip()

# ---------- Validation ----------
valid = True
print("\nValidation Results:")

# 1) ชื่อ: ตัวอักษรกับช่องว่างเท่านั้น
if name.replace(" ", "").isalpha():
    print("Name: Valid (contains only letters and spaces)")
else:
    print("Name: Invalid (use letters and spaces only)")
    valid = False

# 2) อายุ: ต้องเป็นตัวเลขก่อน แล้วค่อยแปลงเป็น int
age = 0
if age_str.isdigit():
    age = int(age_str)
    if 18 <= age <= 65:
        print("Age: Valid ({} years old)".format(age))
    else:
        print("Age: Invalid (must be between 18 and 65)")
        valid = False
else:
    print("Age: Invalid (must be a whole number)")
    valid = False

# 3) เบอร์โทร: ตัวเลข 10 หลักพอดี
if phone.isdigit() and len(phone) == 10:
    print("Phone: Valid (10-digit number)")
else:
    print("Phone: Invalid (must be exactly 10 digits)")
    valid = False

# ---------- Formatted output ----------
if valid:
    if age <= 30:
        age_group = "Young Adult (18-30)"
    elif age <= 50:
        age_group = "Adult (31-50)"
    else:
        age_group = "Senior Adult (51-65)"

    print("\nFormatted Information:")
    print("Name: %s" % name.upper())
    print("Age Group: %s" % age_group)
    print("Phone: +91-{}".format(phone))
else:
    print("\nPlease correct the invalid information and try again.")