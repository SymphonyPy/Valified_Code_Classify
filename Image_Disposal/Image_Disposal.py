import os
import Crop
import OSTU

read_path = "D:\Code\Python\Valified_Code_Classify\\raw"
save_path = "D:\Code\Python\Valified_Code_Classify\\temp"
list = os.listdir(read_path)
num = 0
for i in list:
    num += 1
    print("picture " + str(num))
    its_path = read_path + "\\" + i
    pic = OSTU.OSTU(its_path)
    Crop.Crop(pic, save_path, i)
