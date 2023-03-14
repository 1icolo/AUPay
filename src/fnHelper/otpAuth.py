import random
import pyotp
from typing import Sequence


def get_random_secret(length: int = 12, chars: Sequence[str] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ234567")) -> str:
    return "".join(random.choice(chars) for _ in range(length))


def get_totp(secret):
    return pyotp.TOTP(secret)


def verify_otp(totp, otp):
    return pyotp.TOTP.verify(totp, otp)

    
# generate random and save the TOTP somewhere
# ask the user to input manually the secret key to authenticator app
# input the OTP from the authenticator app
# verify the input
