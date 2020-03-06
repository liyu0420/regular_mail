# grafana_dashboard_mail
定时发送Grafana的Dashboard面板图日报邮件

- main.py：入口文件

- get_grafana_dashboard.py：通过组装url下载指定时间区间的日报dashboard图片

- send_mail.py：发送日报邮件或者下载失败的体型邮件

- schedule：第三方定时器库（https://github.com/dbader/schedule）

- rm_picture.py：删除生成的图片

- config.py: 配置文件

  

配置文件详解：

- grafana_server：grafana server 地址

  eg.'http://ip:端口'

- header ：grafana api 访问鉴权

  eg. {"Authorization": "Bearer APIKEY"}

- dashboard_list : 要访问的图标信息

  eg. [['图表名称',"图表dbuid",'其他参数(&var-node=xxxx)'],['图表名称',"图表dbuid",'其他参数(&var-node=xxxx)']

  

  #邮件发送相关信息  

- gserver : 'smtp.qq.com'
  gport :25
  username : 发送邮箱的名称
  password : 邮箱的授权码
  mailfrom ： 发送邮件的邮箱地址
  mailto ： 邮件接收方邮箱地址   eg. mailto = [mail1'','mail2']
  mailcc ： 邮件抄送方邮箱地址
  subject ： 邮件主题

