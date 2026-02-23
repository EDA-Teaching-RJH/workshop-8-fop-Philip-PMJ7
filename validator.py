import re
import csv

def is_valid_email(email):
    # Returns True if it matches our final rule from Part 4, otherwise False
    if re.search(r"^\w+@\w.+\.(ac.uk|gov.uk|nhs.net)$", email):
        return True
    return False

def main():
    email = input("What's your email? ").strip()
    name = input("What's your name? ").strip()

    if is_valid_email(email):
        print("Valid email. Saving to contacts...")
        with open("contacts.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "email"])
            writer.writerow({"name": name, "email": email})
    else:
        print("Invalid email. Not saved.")

if __name__ == "__main__":
 main()
