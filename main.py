import qrcode
import cv2 
import os

 # qr code generator 
url = input("Enter the URL: ").strip()

file_path = os.path.join(os.getcwd(), "qrcode.png")   # To this runs on ANY computer


qr = qrcode.QRCode()
qr.add_data(url)
image = qr.make_image()
image.save(file_path)

print("qr code is generated ")

 # qr code reader

choice = input("Do you want to scan a QR code now? (yes/no):").lower()

if choice == "yes":
    cap = cv2.VideoCapture(0)  # this Open camera
    detector = cv2.QRCodeDetector()
    last_scanned = ""

    print("Scanning... Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        for qr_code in decode(frame):
            data = qr_code.data.decode("utf-8")
            print("QR Code Detected:", data)

        cv2.imshow("QR Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()