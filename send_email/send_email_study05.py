'''
如果构造一个MIMEText对象，就表示一个文本邮件对象
如果构造一个MIMEImage对象，就表示一个作为附件的图片对象，
要把多个对象组合起来，就用MIMEMultipart对象，他代表的是整个邮件。
'''

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#邮箱服务器配置信息
smtp_server ='smtp.qq.com'  #qq邮箱服务器
port=465

#邮件发送人和收件人信息
send_eamil = '1976085712@qq.com'  # 发送方邮箱
password = 'vnhakqrqvuopdgeh'  # 填入发送方邮箱的授权码
receiver_mail = 'a1976085712@163.com'  # 收件人邮箱


# 设置总的邮件体对象，对象类型为mixed
msg = MIMEMultipart('mixed')

# 构建邮件文本内容
text_info = "这是我使用python smtplib及email模块发送的邮件"
text_sub  = MIMEText(text_info,'plain','utf-8')
msg.attach(text_sub)

# 构建.txt文件邮件附件
txt_file = open(r'E:\GitHub\Python_Study\send_email\20200228.txt', 'rb').read()
txt  = MIMEText(txt_file, 'base64', 'utf-8')
txt ["Content-Type"] = 'application/octet-stream'
txt .add_header('Content-Disposition', 'attachment', filename='text.txt')
msg.attach(txt)

# 构建html格式邮件附件
html_info=open(r'E:\GitHub\Python_Study\send_email\cnode.html','rb').read()
html_sub  = MIMEText(html_info, 'html', 'utf-8')
html_sub ["Content-Disposition"] = 'attachment; filename="csdn.html"'
msg.attach(html_sub)

# 构建.png图片格式邮件附件
image_file = open(r'E:\GitHub\Python_Study\send_email\tupian.png', 'rb').read()
image  = MIMEImage(image_file)
image .add_header('Content-ID', '<image1>')
image ["Content-Disposition"] = 'attachment; filename="red_people.png"'
msg.attach(image)


#构建邮件主题和邮件头部发送人、收件人信息
subject = "python邮件测试"
msg['Subject'] = Header(subject,'utf-8')
msg['From'] = send_eamil
msg['To'] = receiver_mail


try:
    server=smtplib.SMTP_SSL(smtp_server,port)   #链接服务器
    server.login(send_eamil,password)   #登录邮箱
    server.sendmail(send_eamil,receiver_mail,msg.as_string())   #发送邮件
    print('success')
except Exception:
    print('fail')
finally:
    server.quit()
