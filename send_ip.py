#!/usr/bin/env python2.7
import smtplib, string, subprocess
import time, urllib

def check_network():
    while True:
        try:
            result=urllib.urlopen('http://baidu.com').read()
            print result
            print "Network is Ready!"
            break
        except Exception , e:
           print e
           print "Network is not ready,Sleep 5s...."
           time.sleep(5)
    return True

check_network()

# Settings
fromaddr = 'qq859755014@126.com'
toaddr = 'qq859755014@126.com'

# Googlemail login details
username = 'qq859755014@126.com'
password = '1password2'

output_date = subprocess.Popen(['date|cut -d " " -f 2-4'], stdout=subprocess.PIPE, shell=True).communicate()[0]
output_ip = subprocess.Popen(['/opt/vc/bin/vcgencmd measure_temp | cut -b 6-11'], stdout=subprocess.PIPE, shell=True).communicate()[0]
output_temp = subprocess.Popen(['curl ident.me'], stdout=subprocess.PIPE, shell=True).communicate()[0]

send_date = "Boot time: %s" % (output_date)
send_ip = "Temperature: %s" % (output_ip)
send_temp = "External IP: %s" % (output_temp)

BODY = string.join((
"From: %s" % fromaddr,
"To: %s" % toaddr,
"Subject: Your RasPi just booted @ %s" % (output_date),
"",
send_date,
send_ip,
send_temp,
), "\r\n")




# send the email
server = smtplib.SMTP('smtp.126.com')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, BODY)
server.quit()
