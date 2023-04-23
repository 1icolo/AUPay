import pyotp
import qrcode
from PIL.ImageQt import ImageQt
from PyQt5 import QtGui


def get_random_secret():
    return pyotp.random_base32()


def get_totp(secret):
    return pyotp.TOTP(secret)


def verify_otp(totp, otp):
    return pyotp.TOTP.verify(totp, otp)


def generate_qr(secret_key, school_id, issuer="AUP"):
    uri = f'otpauth://totp/{issuer}:{school_id}?secret={secret_key}&issuer={issuer}'
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(uri)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('temp/qr_code.png')
    qimg = ImageQt(img)
    return QtGui.QImage(qimg)