import os
import time
from PIL import Image


# 批量修改图片尺寸，输入原图目录和修改后存放目录地址即可
def resize_batch(path, save_path):
    files = os.listdir(path)  # 返回path目录下的所有文件名

    # 遍历每一张图片并修改其尺寸
    for i in files:
        f = 0
        document = os.path.join(path, i)  # 返回path和i拼接之后的路径，即第i张图片
        img = Image.open(document)  # 读取第i张图片
        img_resize = img.resize((637, 800))  # 修改为100x128尺寸
        fileName = str(i)[:-4]  # 原图除后缀外的名字，这里原图后缀是.jpg
        img_resize.save(save_path + os.sep + '%s.jpg' % fileName)  # 保存路径，其中os.sep为系统分隔符


if __name__ == '__main__':
    resize_batch('demo', "demo")