import re

email = input("What's your email? ").strip()
if re.search(r"^\w+@\w.+\.ac.uk$", email):
    print("Well done.")

phone_number = input("Please enter your phone number: ")
if re.search(r"^07\d{9}$", phone_number):
    print("Very nice.")


student_id = input("Please enter your student ID: ")
if re.search(r"^\w{4}+\d{4}$", student_id):
    print("Very nice.")
else:
    print("You dun goofed.")