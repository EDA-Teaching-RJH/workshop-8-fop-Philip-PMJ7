import re

def is_valid_email(email):
    # Returns True if it matches our final rule from Part 4, otherwise False
    if re.search(r"^\w+@\w.+\.(ac.uk|gov.uk|nhs.net)$", email):
        return True
    return False

def main():
    email = input("What's your email? ").strip()
    if is_valid_email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
 main()
