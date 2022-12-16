from faker import Factory
import random

fake = Factory.create()

FIRSTNAME_NEW = fake.first_name()
LASTNAME_NEW = fake.last_name()
EMAIL_NEW = fake.email()
PHONE_NEW = fake.phone_number()
PASSWORD = "qwerty"
NON_EXISTING_USERNAME = "NON_EXISTING_USERNAME"+str(random.randint(0, 10))
WRONG_PASSWORD = "WRONG_PASSWORD"

MIN_WAIT = 1
H1_FONT_SIZE = 33
H1_FONT_COLOR = "rgba(68, 68, 68, 1)"