#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = 'Liangmingli'
import sys
import requests
from .Sender import mail



server = '64.137.241.113'
TIMEOUT = 5
URL = 'https://www.google.com'


if __name__ == "__main__":
    subject = sys.argv[1]
    message = sys.argv[2]
    try:
        respone = requests.get(URL,timeout = TIMEOUT)
    except:
        print("send email")

    ret = mail(title=subject,message=message,senderName=server)
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")