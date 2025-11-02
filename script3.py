print ("=== BULK PASSWORD AUDITOR ===")
print ("scanning multi password...\n")
passwords = ["abc", "password", "Secret123", "admin2025", "letmein"]

weak_count = 0

for password in passwords:
    print(f"Checking: {password}")
    length = len(password)
    if length >=8 and any(char.isdigit() for char in password) and any(not char.isalnum() for char in password) and any(char.isupper() for char in password) and any(char.islower() for char in password):
        print("This is very strong password")
    else:
        print("WEAK")
        weak_count +=1
        if length <8:
            print("   Too short")
        if not any( char.isupper() for char in password):
            print("   No Upper Case")
        if not any( char.islower() for char in password):
            print("   No Lower Case")
    print("----")
print(f"\n AUDIT COMPLETE : {weak_count} WEAK PASSWORDS FOUND")