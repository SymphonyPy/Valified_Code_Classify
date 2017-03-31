import os
import Crop
import OSTU

read_path = "D:\Code\Python\Valified_Code_Classify\\raw"
save_path = "D:\Code\Python\Valified_Code_Classify\Dataset"
list = os.listdir(read_path)
for i in list:
    its_path = read_path + "\\" + i
    pic = OSTU.OSTU(its_path)
    Crop.Crop(pic, save_path, i)
