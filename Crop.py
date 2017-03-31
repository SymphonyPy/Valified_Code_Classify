from PIL import Image, ImageOps
import os


def Crop(pic, save_address, save_name):
    amount = len(os.listdir(save_address))
    num = 0
    left = 0
    right = 0
    for i in range(0, 120):
        temp = 0
        for j in range(0, 40):
            if pic.getpixel((i, j)) == 255 and left == 0:
                left = i
                break
            if pic.getpixel((i, j)) == 0 and left:
                temp += 1
            if temp == 40:
                right = i
                break
        if left and right:
            file = save_address + "\\" + str(amount) + "_" + save_name[num] + ".jpg"
            pic1 = pic.crop((left, 0, right, 40))
            width = right - left
            expand = 40 - width
            if expand % 2:
                pic2 = ImageOps.expand(pic1, (int(expand / 2) + 1, 0, int(expand / 2), 0), fill="black")
            else:
                pic2 = ImageOps.expand(pic1, (int(expand / 2), 0, int(expand / 2), 0), fill="black")
            pic2.save(file)
            left = 0
            right = 0
            num += 1
            amount += 1
