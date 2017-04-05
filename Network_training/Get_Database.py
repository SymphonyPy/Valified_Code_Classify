from PIL import Image
import numpy as np
import re
import os
import random


def PIC(file):
    im = Image.open(file)
    im = im.convert("L")
    data = im.getdata()
    return np.array(data).reshape(1, 1600)[0] / 255


def Anwser(file):
    pattern = re.compile("\d+_(.*?).jpg")
    A = re.findall(pattern, file)[0]
    matrix = np.zeros((1, 26))
    matrix[0, ord(A) - 97] = 1
    return matrix[0]


def base(address):
    list = []
    for i in os.listdir(address):
        path = address + "\\" + i
        list.append((PIC(path), Anwser(path)))
    return list


class Data(object):
    def __init__(self, trainset_path, testset_path):
        self.train = base(trainset_path)
        self.test = base(testset_path)
        self.test_images = [i[0] for i in self.test]
        self.test_labels = [i[1] for i in self.test]
        self.order = 0
        self.amount = len(self.train)

    def next_batch(self, num):
        mat_pic = np.zeros((num, 1600))
        mat_ans = np.zeros((num, 26))
        for i in range(0, num):
            mat_pic[i] = self.train[self.order][0]
            mat_ans[i] = self.train[self.order][1]
            self.order = (self.order + 1) % self.amount
        return mat_pic, mat_ans

        # def next_batch(self, num):
        #     list = []
        #     mat_pic = np.zeros((num, 1600))
        #     mat_ans = np.zeros((num, 26))
        #     for i in range(0, num):
        #         order = random.randint(0, self.amount - 1)
        #         if order not in list:
        #             mat_pic[i] = self.train[order][0]
        #             mat_ans[i] = self.train[order][1]
        #             list.append(order)
        #         else:
        #             i -= 1
        #     return mat_pic, mat_ans

# trainset_path = "D:\Code\Python\Valified_Code_Classify\Dataset\\train_set"
# testset_path = "D:\Code\Python\Valified_Code_Classify\Dataset\\test_set"
# a = Data(trainset_path, testset_path)
# print(a.test_images)
# print(a.test_labels)
# print(a.next_batch(2))
