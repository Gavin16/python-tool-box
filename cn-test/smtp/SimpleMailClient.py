"""
    使用邮件账户: kupature@163.com  向任意邮箱发送邮件
"""

from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header


def get_mail_server(sender_email):
    key = sender_email[sender_email.index('@') + 1:]
    return "smtp." + key


port = '25'
sender = 'kupature@163.com'
receiver = 'mingorun@163.com'

mail_server = get_mail_server(sender)
sender_pass = "VPIKJNTBRGRLEAQO"  # sender邮箱对应授权码
mail_msg = '你好mingorun, 这是一封测试邮件。'

msg = MIMEText(mail_msg, 'plain', 'utf-8')
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = Header('测试代码发送邮件', 'utf-8')

try:
    server = SMTP(mail_server, port)
    server.login(sender, sender_pass)
    server.sendmail(sender, receiver, msg.as_string())

    server.quit()
    print("邮件发送成功!")

except IOError:
    server.quit()
    print("邮件发送失败!")
