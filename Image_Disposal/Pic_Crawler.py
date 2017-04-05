import requests as rs
from PIL import Image
import os
import psutil


def Clear_file(path):
    for i in os.listdir(path):
        os.remove(path + "\\" + i)


def Crawler(save_address, num):
    order = 0
    for i in range(0, num):
        order += 1
        print("picture " + str(order))
        get_url = "https://www.c5game.com/api/login/captcha.html?refresh=1"
        pic_url = "https://www.c5game.com" + rs.get(get_url).json()["url"]
        pic = rs.get(pic_url).content
        address = save_address + '\\' + str(i) + '.jpg'
        file = open(address, 'wb')
        file.write(pic)
        file.close()


def Verified(save_address):
    num = 0
    list = os.listdir(save_address)
    for i in list:
        num += 1
        address = save_address + "\\" + i
        pic = Image.open(address)
        pic.show()
        name = input("No." + str(num) + " Input:")
        pic.close()
        for proc in psutil.process_iter():
            if proc.name() == "Microsoft.Photos.exe":
                proc.kill()
        if name:
            os.renames(address, save_address + "\\" + name + ".jpg")


if __name__ == "__main__":
    path = "D:\Code\Python\Valified_Code_Classify\\raw"
    Clear_file(path)
    Crawler(path, 100)
    Verified(path)
