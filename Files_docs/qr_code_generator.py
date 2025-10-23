import qrcode
import qrcode.image.svg as qr

print("Enter the website you need to make QR code: ")
s = input()

q = qrcode.QRCode(version=1,box_size=10, border=5)

q.add_data(s)
q.make(fit=True)

img = q.make_image(fill="black", back_color="white")
img.save("qrcode.jpg")