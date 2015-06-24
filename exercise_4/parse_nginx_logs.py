from timeit import timeit
import re


# Nginx log file
nlog = '192.168.1.12 - - [23/Jun/2015:11:10:57 +0000] "GET /entry/how-create-configure-free-ssl-certificate-using-django-and-pythonanywhere HTTP/1.1" 302 5 "http://www.reddit.com/r/Python/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.18 Safari/537.36" "192.168.1.12"'

# http_x_real_ip verbose
timeit(setup="import re", stmt='''re.findall(r'(\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3})','192.168.1.1 999.999.999.999')''', number=1000000)
#1.6111507180003173

# http_x_real_ip succinct
timeit(setup="import re", stmt='''re.findall(r'(?:\d{1,3}\.){3}\d{1,3}','192.168.1.1 999.999.999.999')''', number=1000000)
#1.7421739230003368

http_x_real_ip = re.search(r'(\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3})', nlog)
