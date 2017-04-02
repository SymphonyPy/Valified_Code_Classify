from PIL import Image


def sigma(im, i, debug=False):
    """
    阈值为i时,图像im中两组的方差
    """
    c0_p_num = sum(im.histogram()[:i + 1])  # 灰度<=k的像素个数
    c1_p_num = sum(im.histogram()[i + 1:])  # 灰度>k的像素个数
    # 计算两部分的总灰度
    c0_g_sum = 0
    for j in range(1, i + 1):
        c0_g_sum += j * im.histogram()[j]
        # end for j
    c1_g_sum = 0
    for j in range(i + 1, 255):
        c1_g_sum += j * im.histogram()[j]
        # end for j
    # 计算两部分的各自平均灰度
    try:
        u0 = 1.0 * c0_g_sum / c0_p_num
        u1 = 1.0 * c1_g_sum / c1_p_num
        # 计算两部分的像素比例
        w0 = 1.0 * c0_p_num / (c0_p_num + c1_p_num)
    except:
        # 可能有的图像没有太高或太低灰度的像素
        return 0
    w1 = 1.0 - w0
    u = (u0 - u1) ** 2
    new_sigma = w0 * w1 * u
    if debug:
         print("%d:\tw0=%f,w1=%f,new_sigma=%f" % (i, w0, w1, new_sigma))
    return new_sigma


def OtsuThreshold(im, debug=False):
    """
    线性查找最大方差,可以考虑用别的搜索算法
    """
    g_level = 0
    g_sigma = 0
    for i in range(1, 255):
        new_sigma = sigma(im, i, debug)
        if g_sigma < new_sigma:
            g_sigma = new_sigma
            g_level = i
    # end for i
    return g_level, g_sigma


def OSTU(src_file):
    im = Image.open(src_file).convert("L")

    # 大津法找阈值
    debug = False
    threshold, max = OtsuThreshold(im, debug)
    # print(threshold, max)

    # 根据阈值,分割之
    im = im.point(lambda p: p > threshold and 255)
    return im
