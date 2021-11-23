import cv2
import os

detector = cv2.QRCodeDetector()
val,_ ,_ = detector.detectAndDecode(cv2.imread("img"+"\\"+input("File Name: ")+".png"))
print("Value:",val)

os.system('git commit -a -m "Added Image!" ')
os.system("git push")