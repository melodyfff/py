# coding=utf-8
# function: python发送smtp邮件

from email.mime.multipart import MIMEMultipart
import smtplib as sl
from email.mime.text import MIMEText
from email.header import Header

mail_host = ''  # 邮件服务器地址
mail_user = ''  # 用户名
mail_pass = ''  # 密码

sender = ''  # 发送者
receivers = ['']  # 接收邮件
subject = '邮件标题'  # 邮件标题


# 纯文本消息
def textMessage(content):
    content = 'Python 邮件发送测试...' if content is None else content
    message = MIMEText(_text=content, _subtype='plain', _charset='utf-8')
    message['Subject'] = subject
    return message


# 构造html消息
def htmlMessage():
    message_html = """
    <h2>你好:</h2>
    <p>Python 邮件发送测试...</p>
    <p><a href="#">这是一个链接</a></p>
    """
    message = MIMEText(_text=message_html, _subtype='html', _charset='utf-8')
    message['FROM'] = Header('发件人测试', 'utf-8')
    message['To'] = Header('收件人测试', 'utf-8')
    message['Subject'] = Header('测试邮件标题', 'utf-8')
    return message


# 带附件的消息
def multipartMessage():
    message = MIMEMultipart()
    message['Subject'] = subject
    message.attach(MIMEText(_text='Python 邮件发送测试...', _subtype='plain', _charset='utf-8'))  # 邮件内容

    attach = MIMEText(_text=open('smtpmail.py', 'rb').read(), _subtype='base64', _charset='utf-8')  # 附件
    attach['Content-Type'] = 'application/octet-stream'
    attach['Content-Disposition'] = 'attachment; filename="smtpmail.py"'  # 附件中显示的名字
    message.attach(attach)
    return message


# 发送邮件
def sendMail(message):
    sto = sl.SMTP()
    sto.connect(mail_host, 25)  # 连接默认端口
    sto.login(mail_user, mail_pass)  # 登录
    sto.sendmail(sender, receivers, message.as_string())
    print("Sending mail to %s success..." % receivers)


try:
    sendMail(textMessage(None))
except sl.SMTPException as ex:
    print("Error: Sending email error! error detail: ", ex)
except Exception as ex:
    print("Error: Sending email error,check your settings! error detail: ", ex)
