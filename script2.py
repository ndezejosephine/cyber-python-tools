print ("=== PASSWORD STRENGTH CHECKER ===")
password = input("Enter your password")
length = len(password)
# hasDigit = any(char.isdigit() for char in password)
# SpecialChar = any(not char.isalnum() for char in password)
# Upp = any(char.isupper() for char in password)
# Low = any(char.islower() for char in password)
# if length >=8 and hasDigit==True and SpecialChar==True and Upp==True and Low==True:
#     print("This is very strong password")
# elif length >=8 and hasDigit==True:
#     print("This is a strong password")
# else:
#     print("This is a weak password")

if length >=8 and any(char.isdigit() for char in password) and any(not char.isalnum() for char in password) and any(char.isupper() for char in password) and any(char.islower() for char in password):
    print("This is very strong password")
else:
    print("Your password should contains: 8 Characters in Lower and Upper Case, Numbers, and Special Charaters")

