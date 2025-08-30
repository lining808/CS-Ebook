import os
import urllib.parse
from PIL import Image
from pathlib import Path


def write_text(file_name, method, text):
    """
    write text to file
    method: 'a'-append, 'w'-overwrite
    """
    with open(file_name, method, encoding='utf-8') as f:
        f.writelines(text)

def write_table(class_dict):
    for chapter, chapter2_list in class_dict.items():
        # 写入1级标题
        chapter_text = f'# {chapter}\n'
        write_text(f'readme.md', 'a', chapter_text)
        for chapter2 in chapter2_list:
            # 写入2级标题
            chapter2_text = f'<details>\n<summary>{chapter2}</summary>\n\n'
            write_text(f'readme.md', 'a', chapter2_text)
            # 生成表格
            img_list = os.listdir(f'images/{chapter}/{chapter2}')
            table = ''
            table_head, table_m, table_tail = '|', '|', '|'
            save_flag = False
            for i, img_name in enumerate(img_list):
                if save_flag:
                    table_head, table_m, table_tail = '|', '|', '|'
                if (i+1) % 5 == 0:
                    table_head += f' <img src="{urllib.parse.quote(f"images/{chapter}/{chapter2}/{img_name}")}" width="150px" /> |\n'
                    table_m += ' --------------------- |\n'
                    table_tail += f' {"<br>".join([img_name.split(".")[0][i:i+10] for i in range(0, len(img_name.split(".")[0]), 10)])} |\n'
                    table += table_head + table_m + table_tail + '\n'
                    save_flag = True
                else:
                    table_head += f' <img src="{urllib.parse.quote(f"images/{chapter}/{chapter2}/{img_name}")}" width="150px" /> |'
                    table_m += ' --------------------- |'
                    table_tail += f' {"<br>".join([img_name.split(".")[0][i:i+10] for i in range(0, len(img_name.split(".")[0]), 10)])} |'
                    save_flag = False
            if save_flag:
                table += '\n</details>\n\n'
            else:
                table += table_head + '\n' + table_m + '\n' + table_tail + '\n</details>\n\n'
            # 写入表格
            write_text(f'readme.md', 'a', table)

def write_head(path= './'):
    text = '''本储存库是一些高质量的计算机科学与技术书籍推荐书单，需要学习的可以按照此书单进行学习进阶，包含了计算机大多数软件相关方向。而且敢承诺一直更新。

<img src="images/bg.jpg"  alt=""/>

## 📘 具体内容

🌟 **计算机基础**（计算机概论、组成原理、操作系统、计算机网络、数据结构、算法等）；

🌟 **编程语言**（C、CPP、C#、Rust、Java、Go、Python、SQL、JavaScript、PHP、Ruby、Matlab、Latex等）；

🌟 **软件工程**（产品经理、软件架构、调试测试等）；

🌟 **数学工具**（基础数学、应用数学等）；

🌟 **大数据**（数据分析、数据挖掘等）；

🌟 **人工智能**（机器学习、深度学习、强化学习等）；

🌟 **生存指南**（生存指南、考证、面试等）。

分类根据个人理解和爱好分类，找不到的可以搜索试试。

<img src="images/class.jpg"  alt=""/>

## 🏆 特点

🌟 **精**

* 书在于精而不在于多;

* 本书库推荐的都是个方向经典书籍。

🌟 **新**

* 本书库推荐保持最新版本。

## 🚀 食用指南

* 推荐的书籍，不提供下载地址，需要的可以通过 [Z-Library](https://zh.zlibrary-east.se)(全球最大的开源图书馆) 检索下载，上面书籍较多。

## ⚠️ 声明

此书库推荐均来源于网络，仅供个人学习参考，不提供书籍下载地址，需要的可以自行网络搜索或购买纸质书籍。

<img src="images/start.jpg" alt=""/>

'''
    write_text(f'{path}/readme.md', 'a', text)

def write_tail(path= './'):
    text = '''<img src="images/end.jpg"  alt=""/>

## 🤔 关于本人

<details>
<summary> 简介 </summary>

本人AI算法菜鸡一枚，因此书库中Python、Cpp、人工智能方面的推荐书籍可能更全面一些。以下是自己绘制的AI算法技术栈，有不足的地方希望大家指正。

<img src="images/dl.svg"  alt=""/>
</details>

## 🔄 更新计划

🌟 增加更多的方向

🌟 增加英文书籍

🌟 细分各领域

## 🎉 看这里

如果大家觉得有其他经典的书籍本库没有收录的，欢迎PR。

欢迎star⭐ ，您的关注是我更新的动力。

## 🤝 致谢

* 感谢全体网友的分享
* 感谢全体网友的关注

---

<div style="text-align:center">
  <a href="https://star-history.com/#lining808/CS-Ebook&Date">
    <img src="https://api.star-history.com/svg?repos=lining808/CS-Ebook&type=Date" alt="Star History Chart">
  </a>
</div>
'''
    write_text(f'{path}/readme.md', 'a', text)

def resize_batch(path):
    pat = os.listdir(path)
    for p in pat:
        all_files = [str(file) for file in Path(p).rglob("*") if file.is_file()]
        # 遍历每一张图片并修改其尺寸
        for file in all_files:
            img = Image.open(file)
            img_resize = img.resize((637, 800))
            img.close()
            os.remove(file)
            fileName = file.split('.')[0]
            img_resize.save(f'{fileName}.jpg', format='JPEG', quality=90, dpi=(300, 300))  # 保存路径，其中os.sep为系统分隔符
            # img_resize.save(f'{fileName}.jpg'.replace('（', '(').replace('）', ')'), format='JPEG', quality=90, dpi=(300, 300))  # 保存路径，其中os.sep为系统分隔符


def generate_language_dict(root_dir='./'):
    """
    将文件夹结构转换为字典格式，键为顶级文件夹名，值为子文件夹列表

    参数:
        root_dir (str): 根目录路径，默认为当前目录

    返回:
        dict: 格式如 {'编程语言': ['C', 'Cpp', 'Java']}
    """
    dc = {}
    # 检查根目录是否存在
    if not os.path.exists(root_dir):
        raise FileNotFoundError(f"目录不存在: {root_dir}")

    # 查找顶级文件夹（如'编程语言'）
    top_level_dirs = []
    for entry in os.scandir(root_dir):
        if entry.is_dir():
            top_level_dirs.append(entry.name)

    if not top_level_dirs:
        return {}
    for item in top_level_dirs:
        # 假设只有一个顶级文件夹（根据需求）
        main_dir_name = item
        main_dir_path = os.path.join(root_dir, main_dir_name)

        # 获取子文件夹列表
        sub_dirs = []
        for entry in os.scandir(main_dir_path):
            if entry.is_dir():
                sub_dirs.append(entry.name)
        dc[main_dir_name] = sub_dirs
    return dc


if __name__ == '__main__':
    resize_batch(f'images')

    class_dict = generate_language_dict(f'images')
    if os.path.exists(f'readme.md'):
        os.remove(f'readme.md')

    write_head()
    write_table(class_dict)
    write_tail()

