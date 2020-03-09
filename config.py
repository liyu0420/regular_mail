#grafana server
grafana_server = grafana_server
#grafana 访问header用于鉴权
header = {"Authorization": "Bearer apikey"}
#图表信息：[名称,dbuid,必须的链接参数]
dashboard_list = [['ceph-cluster',"dbuid",''],['linux-47.210',"dbuid",'&var-node=10.0.47.211:9100'],['linux-47.211',"dbuid",'&var-node=10.0.47.210:9100']]
#邮件发送相关信息  
gserver = 'smtp.qq.com'
gport = 25
username = 'xxxxxxx@qq.com' #发送邮箱的名称
password = 'xxxxxxxxxxx' #发送邮箱的授权码
mailfrom = 'xxxxxxxxx@qq.com' #发送邮箱
mailto = ['xxxxxx@foxmail.com','xxxxxxx@qq.com']  #邮件接收方
mailcc = 'xxxxxxx@qq.com' #邮件抄送方
subject = '邮件主题' #邮件主题