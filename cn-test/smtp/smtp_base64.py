"""
    生成base64 编码

"""
import base64
if __name__ == '__main__':
    mail_address = 'kupature@163.com'
    encode_mail = base64.b64encode(mail_address.encode('utf-8'))
    print(encode_mail)
    encode_str = str(encode_mail, 'utf-8')
    print("mail_address encoded:", encode_str)

    active_code = "VPIKJNTBRGRLEAQO"
    active_code_base64 = base64.b64encode(active_code.encode('utf-8'))
    print(active_code_base64)
    print(str(active_code_base64, 'utf-8'))



