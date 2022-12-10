"""
    使用SMTP 协议发送邮件 && pop3接收邮件

    一 邮件发送(以网易邮箱为例):
    # 需要在邮箱设置中 新增授权密码
    minsky@Fm-Mac ~ % telnet smtp.163.com 25
    Trying 220.181.15.161...
    Connected to smtp.163.com.
    Escape character is '^]'.
    220 163.com Anti-spam GT for Coremail System (163com[20141201])
    helo smtp
    250 OK
    auth login
    334 dXNlcm5hbWU6
    a3VwYXR1cmVAMTYzLmNvbQ==
    334 UGFzc3dvcmQ6
    VlBJS0pOVEJSR1JMRUFRTw==
    235 Authentication successful
    mail from:<kupature@163.com>
    250 Mail OK
    rcpt to:<mingorun@163.com>
    250 Mail OK
    data
    354 End data with <CR><LF>.<CR><LF>
    Subject: test

    hello there

    .
    250 Mail OK queued as smtp7,C8CowABnaxjNKXRjjA_pRw--.60209S2 1668557428
    quit
    221 Bye



    二 接收邮件(使用网易邮箱)


"""