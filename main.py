# import qrcode
# import cv2 
# import os

#  # qr code generator 
# url = input("Enter the URL: ").strip()

# file_path = os.path.join(os.getcwd(), "qrcode.png")   # To help to runs on ANY computer


# qr = qrcode.QRCode()
# qr.add_data(url)
# image = qr.make_image()
# image.save(file_path)

# print("qr code is generated ")

#  # qr code reader

# choice = input("Do you want to scan a QR code now? (yes/no):").lower()

# if choice == "yes":
#     cap = cv2.VideoCapture(0)  # this Open camera
#     detector = cv2.QRCodeDetector()
#     last_scanned = ""

#     print("Scanning... Press 'q' to quit.")

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         data,bbox, _ = detector.detectAndDecode(frame)

#         if data and data != last_scanned:
#             print("QR Code Detected:",data)
#             last_scanned = data

#         cv2.imshow("QR Scanner", frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()
import qrcode
import cv2 
import os

# --- QR Code Generator ---
url = input("Enter the URL: ").strip()

# Saves the image in your current project folder
file_path = os.path.join(os.getcwd(), "qrcode.png") 

qr = qrcode.QRCode()
qr.add_data(url)
image = qr.make_image()
image.save(file_path)

print("qr code is generated")

# --- QR Code Reader ---
choice = input("Do you want to scan a QR code now? (yes/no):").lower()

if choice == "yes" or choice == "y":
    cap = cv2.VideoCapture(0)  
    detector = cv2.QRCodeDetector() # This is the NEW tool replacing 'decode'
    last_scanned = ""

    print("Scanning... Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # [THE FIX]: This line replaces the 'for qr_code in decode' loop
        data, bbox, _ = detector.detectAndDecode(frame)

        if data and data != last_scanned:
            print("QR Code Detected:", data)
            last_scanned = data

        cv2.imshow("QR Scanner", frame)

        # Press 'q' to exit the camera window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()