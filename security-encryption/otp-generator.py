import random
import string

class Otp:
    s_char = string.ascii_lowercase
    b_char = string.ascii_uppercase
    d_char = string.digits

    def __init__(self, length):
        self.length = length

    @property
    def digits(self):
        return ''.join(random.choice(self.d_char) for _ in range(self.length))
    
    @property
    def bd_digits(self):
        chars = self.b_char + self.d_char
        return "".join(random.choice(chars) for _ in range(self.length))
    
    @property
    def sd_digits(self):
        chars = self.s_char + self.d_char
        return "".join(random.choice(chars) for _ in range(self.length))
    
    @property
    def sbd_digits(self):
        chars = self.s_char + self.b_char + self.d_char
        return "".join(random.choice(chars) for _ in range(self.length))
    
otp = Otp(10)
print("Digits otp: ", otp.digits)
print("BD otp: ", otp.bd_digits)
print("SD otp: ", otp.sd_digits)
print("SBD otp: ", otp.sbd_digits)