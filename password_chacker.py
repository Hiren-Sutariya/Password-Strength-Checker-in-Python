password = input("Enter Your Password: ")
password_length = len(password)

if len(password) < 6:
    Strength = "Week"
elif len(password) <= 10:
    Strength = "Mediam"
else:
    Strength = "Strong"

print("Password Strength is: ", Strength)