#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = 'Liangmingli'



import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender='244479222@qq.com'    # 发件人邮箱账号
my_pass = 'qmkmciexiqbxbghh'    # 发件人邮箱密码
my_user='13750024242@qq.com'    # 收件人邮箱账号，我这边发送给自己
def mail(title="菜鸟教程发送邮件测试" ,
         message="填写邮件内容",
         senderName = "FromRunoob"):
    ret=True
    try:
        msg=MIMEText(message,'plain','utf-8')
        msg['From']=formataddr([senderName,my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']=title                # 邮件的主题，也可以说是标题

        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception :  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret

