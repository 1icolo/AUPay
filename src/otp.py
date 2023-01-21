import pyotp

totp = pyotp.TOTP('elcidelcidelcid')
print(totp.now())