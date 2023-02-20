import pyotp

class OTPAuthenticate():
    totp = pyotp.TOTP('elcidelcidelcid')
    print(totp.now())