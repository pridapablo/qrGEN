import qrcode


string = "Text"
# Create a QR code object
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Add the encrypted message to the QR code
qr.add_data(string)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill_color='#2c2d72', back_color='transparent')

# Save the QR code image to a file
img.save('qr.png')
