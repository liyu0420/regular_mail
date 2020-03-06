#grafana server
grafana_server = "http://10.0.47.149:3000"
#grafana 访问header用于鉴权
header = {"Authorization": "Bearer eyJrIjoiMzdOQjJOQ285UUVUSWVHTjF1ODhWME1WMEpvZ2xxdFoiLCJuIjoibWFpbCIsImlkIjoxfQ=="}
#图表信息：[名称,dbuid,必须的链接参数]
dashboard_list = [['ceph-cluster',"r6lloPJmz",''],['linux-47.210',"Bkl9bBYik",'&var-node=10.0.47.211:9100'],['linux-47.211',"Bkl9bBYik",'&var-node=10.0.47.210:9100']]
#邮件发送相关信息  
gserver = 'smtp.qq.com'
gport = 25
username = '825830390@qq.com' #发送邮箱的名称
password = 'krfyhbgcnuhabceg' #发送邮箱的授权码
mailfrom = '825830390@qq.com' #发送邮箱
mailto = ['ly44@foxmail.com','liyu@unicloud.com']  #邮件接收方
mailcc = '15332471769@163.com' #邮件抄送方
subject = 'CEPH客户端使用情况' #邮件主题