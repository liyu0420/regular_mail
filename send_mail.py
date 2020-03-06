# coding: utf8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import parseaddr, formataddr
import time as Time
import config

# 发送dashboard日报邮件
def send_mail(image_list):
    # 邮箱的服务地址
    gserver = config.gserver
    gport = config.gport
    username = config.username
    password = config.password
    
    msg = MIMEMultipart('related')
    msg['from'] = config.mailfrom
    msg['to'] = ','.join(config.mailto)
    #抄送
    msg['Cc'] = config.mailcc
    msg['Reply-To'] = config.mailfrom
    msg['Subject'] = config.subject
    
    is_html = True
    if is_html:
        mail_msg = '<html><body>'
        for i in range(len(image_list)):
            mail_msg += '<p><img src="cid:image%d" height="3000" width="1500"></p>' % (i+1)
        mail_msg += '</body></html>'
        msg.attach(MIMEText(mail_msg, 'html', 'utf-8'))

        for i, img_name in enumerate(image_list):
            with open(img_name, 'rb') as fp:
                img_data = fp.read()
            msg_image = MIMEImage(img_data)
            msg_image.add_header('Content-ID', '<image%d>' % (i+1))
            msg.attach(msg_image)
            image = MIMEImage(img_data, _subtype='octet-stream')
            image.add_header('Content-Disposition', 'attachment', filename=image_list[i])
            msg.attach(image)
    try: 
        smtp = smtplib.SMTP(gserver, gport)
        smtp.login(username,password)
        smtp.sendmail(config.mailfrom, msg['to'].split(','), msg.as_string())
        smtp.quit()
        smtp.close()
        print("邮件发送成功")
    except Exception as err:
        print("Send mail failed. ",err) 
        
# 发送失败提醒邮件
def send_failed_mail():
    # 邮箱的服务地址
    gserver = config.gserver
    gport = config.gport
    username = config.username
    password = config.password
    
    msg = MIMEMultipart('related')
    msg['from'] = config.mailfrom
    msg['to'] = ','.join(config.mailto)
    #抄送
    msg['Cc'] = config.mailcc
    msg['Reply-To'] = config.mailfrom
    time_now = int(Time.time())
    time_local = Time.localtime(time_now)
    dt = Time.strftime("%Y%m%d",time_local)
    msg['Subject'] = '监控日报图获取失败-' + dt
    
    content = MIMEText("Dashboard图片下载失败",'utf-8')
    msg.attach(content)
    
    try:
    
        smtp = smtplib.SMTP(gserver, gport)
        smtp.login(username,password)
        smtp.sendmail(config.mailfrom, msg['to'].split(','), msg.as_string())
        smtp.quit()
        smtp.close()
        print("邮件发送成功")
    except Exception as err:
        print("Send mail failed. ",err) 