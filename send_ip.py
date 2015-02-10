import string, subprocess
import time, urllib

def blink(y,n,t):
  tmp = 0
  while (tmp < t):
    subprocess.Popen(['echo 1 > /sys/devices/platform/leds-gpio/leds/led0/brightness'], stdout=subprocess.PIPE, shell=True).communicate()[0]
    # print("11111")
    time.sleep(y)
    subprocess.Popen(['echo 0 > /sys/devices/platform/leds-gpio/leds/led0/brightness'], stdout=subprocess.PIPE, shell=True).communicate()[0]
    # print("00000")
    time.sleep(n)
    tmp += y+n

  subprocess.Popen(['echo 0 > /sys/devices/platform/leds-gpio/leds/led0/brightness'], stdout=subprocess.PIPE, shell=True).communicate()[0]
  # print("------")

def pulse_blink(t):
  tmp = 0
  print "t= %d" %(t)
  while (tmp < t):
    print(tmp)
    blink(.1,.1,.4)
    time.sleep(.5)
    tmp += 1
    pass
  pass

def check_network_with_blink():
    while True:
        try:
            if flag == 0: #send a mail when internet reconnects
              subprocess.Popen(['sudo python ./send_ip.py'], stdout=subprocess.PIPE, shell=True).communicate()[0] 
              flag = 1
              pass

            result=urllib.urlopen('http://baidu.com').read()
            print result
            print "Network is Ready!"
            blink(.5,.5,5)
            break
        except Exception , e:
           print e
           print "Network is not ready,Sleep 5s...."
           flag = 0
           pulse_blink(5)
    return True

while True:
  check_network_with_blink()
  pass
