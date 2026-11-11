import re
def validate_email(email):

    pattern = r"^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def validate_phone(phone):
    pattern = r"^(\+91|0)?[6-9]\d{9}$"
    return bool(re.match(pattern, phone))

emails = ["test@example.com", "invalid-email", "user@domain.org"]

phones = ["+919876543210", "1234567890", "9876543210"]


for e in emails:

    print(f"{e}: {"Valid" if validate_email(e) else "Invalid"}")

for p in phones:

    print(f"{p}: {"Valid" if validate_phone(p) else "Invalid"}")

print("\nname: shreyansh singh")
print("prn no.: 26013010907")
