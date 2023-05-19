#! /bin/bash

uwsgi --version

#停止uWSGI
#uwsgi --stop /var/run/uwsgi.pid

#使用uwsgi.ini配置文件启动wsgi应用程序
uwsgi --ini uwsgi.ini

##重启uWSGI服务器
#uwsgi --reload /var/run/uwsgi.pid


##查看所有uWSGI进程
#ps aux | grep uwsgi
#ps -eLf | grep uwsgi

##停止所有uWSGI进程
#sudo pkill -f uwsgi -9


