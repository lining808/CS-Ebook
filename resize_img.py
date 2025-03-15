import os
from PIL import Image


# 批量修改图片尺寸，输入原图目录和修改后存放目录地址即可
def resize_batch(path, save_path):
    # 遍历每一张图片并修改其尺寸
    for i in os.listdir(path):
        img = Image.open(os.path.join(path, i))  # 读取第i张图片
        img_resize = img.resize((637, 800))  # 修改为100x128尺寸
        fileName = i.split('.')[0]
        img_resize.save(save_path + os.sep + f'{fileName}.jpg')  # 保存路径，其中os.sep为系统分隔符


if __name__ == '__main__':
    resize_batch('demo', "demo")