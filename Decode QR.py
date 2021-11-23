import cv2

detector = cv2.QRCodeDetector()
val,_ ,_ = detector.detectAndDecode(cv2.imread("\\img"+input("File Name: ")+".png"))
print("Value:",val)