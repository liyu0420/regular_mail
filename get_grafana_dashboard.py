# coding: utf8

import os,stat
import urllib.request
from datetime import datetime, date, time, timedelta
import time as Time
import config

# 获取1天前0点与今日0点的时间戳
def last_time():
    midnight = datetime.combine(date.today(), time.min)
    yesterday_mid = midnight - timedelta(days=1) # 想要此前几天的，就改这个参数
    epoch = datetime.utcfromtimestamp(0)
    midnight = midnight - timedelta(seconds=1)
    midnight = int((midnight - epoch).total_seconds() * 1000.0)
    yesterday_mid = int((yesterday_mid - epoch).total_seconds() * 1000.0)
    return str(yesterday_mid), str(midnight)

# 下载指定的dashboard
def download_db(image_list):
    dashboard_list = config.dashboard_list
    grafana_server = config.grafana_server
    header = config.header
    for i in range(len(dashboard_list)):    
        dbuid = dashboard_list[i][1]     
        url = (grafana_server + '/render/d/' +
                   dbuid + '?from=' +
                   last_time()[0] + '&to=' + last_time()[1] +
                   '&var-datasource=ceph&width=1500&height=3000&tz=Asia%2FShanghai' + dashboard_list[i][2]
                   )       
        # 用管理员去Grafana生成API Key
        request = urllib.request.Request(url,headers=header)
        # noinspection PyBroadException
        try:
        
            # 访问并下载面板图
            response = urllib.request.urlopen(request)
            time_now = int(Time.time())
            time_local = Time.localtime(time_now)
            dt = Time.strftime("%Y-%m-%d",time_local)
            img_name = "img_"+dashboard_list[i][0]+"_"+dt+".png"
            image_list.append(img_name)
            # print(response.getcode())
            if int(response.getcode()) == 200:
                with open(img_name, "wb") as f:
                    f.write(response.read())
               #return img_name
            else:
                return "failed"
        except:
            return "failed"

    
 
