from PIL import Image, ImageOps

pic = Image.open("D:\Code\Python\Valified_Code_Classify\\result.png")
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
        file = "D:\Code\Python\Valified_Code_Classify\\result\\result" + str(num) + ".jpg"
        pic1 = pic.crop((left, 0, right, 40))
        pic1.save(file)
        width = right - left
        expand = 40 - width
        print(width, expand)
        if expand % 2:
            pic2 = ImageOps.expand(pic1, (int(expand / 2) + 1, 0, int(expand / 2), 0), fill="black")
        else:
            pic2 = ImageOps.expand(pic1, (int(expand / 2), 0, int(expand / 2), 0), fill="black")
        pic2.save(file)
        left = 0
        right = 0
        num += 1
