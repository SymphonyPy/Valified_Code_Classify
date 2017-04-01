from PIL import Image
import numpy as np
import re


def PIC(file):
    im = Image.open(file)
    im = im.convert("L")
    data = im.getdata()
    return np.matrix(data).reshape(1, 1600)[0]


def Anwser(file):
    pattern = re.compile("\d+_(.*?).jpg")
    A = re.findall(pattern, file)[0]
    matrix = np.zeros((1, 26))
    matrix[0, ord(A) - 97] = 1
    return matrix[0]
