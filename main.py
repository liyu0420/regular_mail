# coding: utf8

import schedule
import time
import get_grafana_dashboard
import send_mail
import rm_picture

# 获取面板图并发邮件
def do_report():
    #grafana dashboard 图片
    image_list = []
    print("start to report")
    response = get_grafana_dashboard.download_db(image_list)
    if (response == "failed"): # 下载失败，邮件提醒
        send_mail.send_failed_mail()
    else: # 成功则发日报邮件
        send_mail.send_mail(image_list)
    rm_picture.rmpicture()
    print("report end")

# 定时每日8点发送
schedule.every().day.at("13:42").do(do_report)

while True:
    schedule.run_pending()
    time.sleep(1)