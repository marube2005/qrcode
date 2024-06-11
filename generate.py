#Install all hthe Libraries needed.
#Create a function that collect a text and converts it to a qrcode
#Save the qrcode as an image.
#Calll the function.

import qrcode

def qr_code(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")
    print("QR Code Created")

url = input("Enter your url: ")
qr_code(url)
