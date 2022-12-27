import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@gmail.com')
regpx = re.compile(r'[0-9]{10}')

def isValidEmail(email):
    if re.fullmatch(regex, email):
      print("Valid email")
    else:
      print("Invalid email")

def isValidPhone(Phone):
    if re.fullmatch(regpx, Phone):
      print("Valid Phone")
    else:
      print("Invalid Phone")