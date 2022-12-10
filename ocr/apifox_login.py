"""
    APIFox 业务接口调用前，先进行登录操作，具体步骤如下:
    (1) 请求接口获取验证码内容
    (2) 验证码内容base64 转图片存储
    (3) 使用OCR 识别图片内容
    (4) 返回识别结果文本给到 APIFox

"""

import ddddocr
import base64

import requests
import json
import hashlib

from requests.packages import urllib3

# 覆盖保存
image_path = '/Users/minsky/PycharmProjects/captcha/image.png'

"""
    base64编码转图片存储
"""


def base64_to_image(base64_str: str, file_path: str):
    prefix_and_body = base64_str.split(",")
    info_str = prefix_and_body[1]
    image_data = base64.b64decode(info_str)
    file = open(file_path, 'wb')
    file.write(image_data)
    file.close()


"""
    图片内容识别
    识别验证码输出到控制台后, APIFox可以读取到    
"""


def image_ocr(file_path):
    ocr = ddddocr.DdddOcr()
    with open(file_path, 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    f.close()
    return res


"""
    请求指定地址获取验证码Base64 字符串
"""


def get_captcha():
    urllib3.disable_warnings()
    captcha_url = 'https://103.135.199.81:3031/api/sso/captcha'
    header = build_request_header()
    res = requests.post(captcha_url, header, verify=False)
    res_dict = json.loads(res.content)
    base64_str = res_dict['data']
    # print(base64_str)
    set_cookie = res.headers.get("set-cookie")
    captcha_md5 = parse_captcha_code_md5(set_cookie)

    return base64_str, captcha_md5


def build_request_header():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
        'Cookie': 'gkx_sso_username=wfm; gkx_sso_pwd=FB565DFAB51527B68CBB882A4E84DD57',
        'Referer': 'https://103.135.199.81:3031/?appid=label-platform&callback=https%3A%2F%2F103.135.199.81%3A3030' +
                   '%2Ftask',

    }
    return header


"""
    从请求的响应头中获取验证码 MD5摘要
"""


def parse_captcha_code_md5(field_value):
    values = field_value.split(',')
    k_v = values[0].split("=")
    return k_v[1]


if __name__ == '__main__':
    # POST 请求获取验证码
    b64_str, cap_md5 = get_captcha()

    base64_to_image(b64_str, image_path)
    captcha = image_ocr(image_path)
    print(captcha, ",", cap_md5)
    # regain_md5 = hashlib.md5(captcha.encode()).hexdigest().upper()
    # print(cap_md5)
    # print("captcha equals in md5:", cap_md5.__eq__(regain_md5))

