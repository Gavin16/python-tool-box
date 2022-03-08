# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


"""
 => ddddocr 安装方式:
1. 安装 pip (如果有可以跳过)
2. 安装pip
   pip install ddddocr -i https://pypi.tuna.tsinghua.edu.cn/simple

以上安装建议单独新建一个虚拟环境

"""

"""
这里展示图片从本地读取, 实际可以根据需要从网络获取,最后转化为字节数组即可

=> 图片存储位置为本地, 图片文件名: img.png
"""

import ddddocr


def image_ocr():
    ocr = ddddocr.DdddOcr()
    with open('img.png', 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)

    print(res)


if __name__ == '__main__':
    image_ocr()
