from timeit import timeit
import re


# Nginx log file
nlog = '192.168.1.12 - - [23/Jun/2015:11:10:57 +0000] "GET /entry/how-create-configure-free-ssl-certificate-using-django-and-pythonanywhere HTTP/1.1" 302 5 "http://www.reddit.com/r/Python/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.18 Safari/537.36" "192.168.1.12"'

# Full regex statement
r = re.search(r'(\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3}) - - \[(.*)\] \"(\w{0,4}.* \w{0,4}/\d\.\d)\" (\d+) (\d+) "(\S+)" ["](.*)["] ["](\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3})', nlog)

http_x_real_ip = r.groups()[0]
# print(http_x_real_ip)
time_local = r.groups()[1]
# print(time_local)
request = r.groups()[2]
# print(request)
status = r.groups()[3]
# print(status)
body_bytes_sent = r.groups()[4]
# print(body_bytes_sent)
http_referer = r.groups()[5]
# print(http_referer)
http_user_agent = r.groups()[6]
# print(http_user_agent)
http_x_forwarded_for = r.groups()[7]
# print(http_x_forwarded_for)

# http_x_real_ip verbose
# print(timeit(setup="import re", stmt='''r = re.search(r'(\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3})', '192.168.1.1 999.999.999.999')''', number=1000000))
# 1.159849308001867

# http_x_real_ip succinct
# print(timeit(setup="import re", stmt='''r = re.search(r'((?:\d{1,3}\.){3}\d{1,3})', '192.168.1.1 999.999.999.999')''', number=1000000))
# 1.7421739230003368

# http_x_real_ip = re.search(r'(\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3})', nlog)
# print(http_x_real_ip.groups()[0])

# time_local verbose
# print(timeit(setup="import re", stmt='''r = re.search(r'(\d{2}/\w{3}/[2][0]\d{2}:\d{2}:\d{2}:\d{2}\s[+][0]{4})', "[23/Jun/2015:11:10:57 +0000]")''', number=1000000))
# 1.46203494072

# time_local succinct
# print(timeit(setup="import re", stmt='''r = re.search(r'(\[.*\])', "[23/Jun/2015:11:10:57 +0000]")''', number=1000000))
# 1.04375910759

# time_local = re.search(r'(\[.*\])', nlog)
# print(time_local.groups()[0])

# request verbose
# print(timeit(setup="import re", stmt='''r =re.search(r'\"(\w{0,4}.* \w{0,4}/\d\.\d)','GET /entry/how-create-configure-free-ssl-certificate-using-django-and-pythonanywhere HTTP/1.1')''', number=1000000))
#1.277367499016691

# request succinct
# print(timeit(setup="import re", stmt='''r = re.search(r'"(.*)" \d','GET /entry/how-create-configure-free-ssl-certificate-using-django-and-pythonanywhere HTTP/1.1')''', number=1000000))
# 1.4014256190275773

# request = re.search(r'\"(\w{0,4}.* \w{0,4}/\d\.\d)', nlog)
# print(request.groups()[0])

# request, body_bytes_sent verbose
# print(timeit(setup="import re", stmt='''r = re.search(r' (\d\d\d) (\d+)','HTTP/1.1" 302 5949502 "http:')''', number=1000000))
# 2.312330122978892

# request, body_bytes_sent succinct
# print(timeit(setup="import re", stmt='''r = re.search(r' (\d+) (\d+)','HTTP/1.1" 302 5949502 "http:')''', number=1000000))
# 2.1297434479929507

# r = re.search(r' (\d+) (\d+)', nlog)
# status = r.groups()[0]
# body_bytes_sent = r.groups()[1]
# print(status, body_bytes_sent)

# http_referer verbose
# print(timeit(setup="import re", stmt='''r = re.search(r'(\w{3,5}://\S+)"','302 5 "http://www.reddit.com/r/Python/" "Mozilla/5.0')''', number=1000000))
# 2.963139974977821

# http_referer succinct
# print(timeit(setup="import re", stmt='''r = re.search(r'\d "(\S+)"','302 5 "http://www.reddit.com/r/Python/" "Mozilla/5.0')''', number=1000000))
# 2.5299302529892884

# r = re.search(r'\d "(\S+)"', nlog)
# http_referer = r.groups()[0]
# print(http_referer)

# http_user_agent succinct
# print(timeit(setup="import re", stmt='''r = re.search(r'["] ["](.*)["] ["]',' "GET /entry/how-create-configure-free-ssl-certificate-using-django-and-pythonanywhere HTTP/1.1" 302 5 "http://www.reddit.com/r/Python/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.18 Safari/537.36" "192.168.1.12')''', number=1000000))
# 2.240282804996241

# r = re.search(r'["] ["](.*)["] ["]', nlog)
# http_user_agent = r.groups()[0]
# print(http_user_agent)

# Full regex statement
# print(timeit(setup="import re", stmt='''r = re.search(r'(\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3}) - - \[(.*)\] \"(\w{0,4}.* \w{0,4}/\d\.\d)\" (\d+) (\d+) "(\S+)" ["](.*)["] ["](\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3})','192.168.1.12 - - [23/Jun/2015:11:10:57 +0000] "GET /entry/how-create-configure-free-ssl-certificate-using-django-and-pythonanywhere HTTP/1.1" 302 5 "http://www.reddit.com/r/Python/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.18 Safari/537.36" "192.168.1.12"')''', number=1000000))
# 10.371555257006548
