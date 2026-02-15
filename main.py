import qrcode

url = input("Enter the URL: ").strip()

file_path = "C:\\Users\\Vikash_Choudhary\\Desktop\\qrcode.png"
 

qr = qrcode.QRCode()
qr.add_data(url)

image = qr.make_image()
image.save(file_path)

print("qr code is generated ")