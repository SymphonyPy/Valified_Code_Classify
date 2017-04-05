import os
import re


def Anwser(file):
    pattern = re.compile("\d+_(.*?).jpg")
    A = re.findall(pattern, file)[0]
    return A


file = "D:\Code\Python\Valified_Code_Classify\Dataset\\train_set"
num = 0
list = list(os.listdir(file))
list.sort()
for i in list:
    num += 1
    old_path = file + "\\" + i
    new_path = file + "\\" + str(num) + "_" + Anwser(file + "\\" + i) + ".jpg"
    try:
        os.renames(old_path, new_path)
        print(i + " --> " + str(num) + "_" + Anwser(file + "\\" + i) + ".jpg")
    except:
        pass
