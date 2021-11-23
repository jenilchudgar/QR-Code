import qrcode
import os

img = qrcode.make(input("Enter data: "))
img.save("img\\"+input("File Name: ")+".png")

os.system("git add .")
os.system('git commit -a -m "Added Image!" ')
os.system("git push")