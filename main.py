from datetime import date
import re
import base64
import pathlib
from art import tprint

list_a = []

class Worker:
    def __init__(self, surname, name, birth_year, email, mobile_number, date, address, image, is_admin):
        self.surname = surname
        self.name = self._is_valid_name(name)
        self.birth_year = self._is_valid_birth_year(birth_year)
        self.email = self._is_valid_email(email)
        self.mobile_number = self._is_valid_mobile_number(mobile_number)
        self.date = date
        self.address = address
        self.image = self.add_image(image)
        self.is_admin = is_admin

    @classmethod
    def _is_valid_name(self, name):
        valid_name = bool(re.search(r'\d', name))
        if (valid_name != False):
            raise ValueError("Validation Error: Name must contain text only")
        else:
            return name

    def _is_valid_birth_year(self, birth_year):
        valid_birth_year = int(birth_year)
        if (valid_birth_year < 0):
            valid_birth_year = 2000
        else:
            return birth_year

    def _is_valid_email(self, email):
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if not re.match(regex, email):
            return email + "@gmail.com"
        return email

    def _is_valid_mobile_number(self, mobile_number):
        return re.sub("\D", "", mobile_number)

    def full_name(self):
        print(f'[+] <{self.name} {self.surname}>{self.email}\n')

    def test(self):
        print(self.image)

    def add_image(self, image_name):
        file_extension = pathlib.Path(image_name).suffix

        if (file_extension != "jpg"):
            with open(image_name, "rb") as image2string:
                converted_string = base64.b64encode(image2string.read())
            return converted_string
        else:
            raise ValueError("The image must not have the .jpg extension.")

    def save_image(self):
        image_64_decode = base64.b64decode(self.image)
        # create a writable image and write the decoding result
        image_result = open('foto.jpg', 'wb')
        image_result.write(image_64_decode)


class Accounting:
    def __init__(self, date=date.today(), type="", weight="", volume=""):
        self.date = str(date)
        self.type = str(type)
        self.weight = float(weight)
        self.volume = float(volume)

    def show_garbage_info(list):
        for obj in list:
            print("[+]",
                "Date:", obj.date,
                "- Garbage type:", obj.type,
                "- Garbage weight:", round(obj.weight, 3),
                "- Garbage volume:", round(obj.volume, 3),
                "- Garbage density:", round(obj.weight / obj.volume, 3))

    def weight_or_volume_calculation(list, weight_or_volume):
        float_sum = 0
        if (weight_or_volume == "weight"):
            for obj in list:
                float_sum += float(obj.weight)
            print("\n" + "[+] " + "Sum of weight:", float_sum)
        elif (weight_or_volume == "volume"):
            for obj in list:
                float_sum += float(obj.volume)
            print("\n" + "[+] " + "Sum of volume:", float_sum)


    def total_calculation(list):
        float_weight = 0
        float_volume = 0
        float_density = 0
        for obj in list:
            float_weight += float(obj.weight)
            float_volume += float(obj.volume)
            float_density += round(float(obj.weight / obj.volume), 3)
        print("\n[+] Sum of weight:", float_weight)
        print("[+] Sum of volume:", float_volume)
        print("[+] Sum of density:", float_density)
        print("------------------------------")
        print("[+] Sum of total:", float_weight + float_volume + float_density, "\n")

tprint("Garbage Accounting")

# Creating an object (volunteer / administrator)
test1 = Worker(
    str("Surname"),  # Surname
    "Name",  # Name
    int(1485),  # Birth Year
    "test.test@test.com",  # Email
    "23984234",  # Mobile number
    date.today(),  # Creation date
    str("test address"),  # Address
    "test1.png",  # There is two images in directory
    True)  # (True, False)

# Data output in the format <First Name Last Name>Mail
test1.full_name()

# Saving pictures to a catalog with image name: photo.jpg
test1.save_image()

# Generate garbage collection data
list_a.append(Accounting(date="2023-01-01", type="Plastic", weight=8.0, volume=2))
list_a.append(Accounting(date="2023-01-01", type="Paper",   weight=50,  volume=15))
list_a.append(Accounting(date="2023-01-01", type="Paper",   weight=60,  volume=20))
list_a.append(Accounting(date="2023-01-01", type="Glass",   weight=120, volume=70))
list_a.append(Accounting(date="2023-01-02", type="Paper",   weight=60,  volume=20))
list_a.append(Accounting(date="2023-01-02", type="Glass",   weight=120, volume=70))

Accounting.show_garbage_info(list_a)

# Counting the mass or volume of the passed garbage type (weight or volume)
Accounting.weight_or_volume_calculation(list_a, "weight")

# Calculation of total data for all time
Accounting.total_calculation(list_a)