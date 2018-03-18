# 导入模块
from wxpy import *
import socket
import threading
import threading
import telnetlib,sys
# 初始化机器人，扫码登陆
bot = Bot()
#bot.join()

#sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sk.settimeout(1)
def fun_timer():
    try:
      telnetlib.Telnet('106.14.18.151','40001')
      print ('Server port 40001 OK!')
    except Exception:
      my_friend = bot.friends().search('爱上百合花')[0]
      my_friend.send('Server port 40001 not connect!');
      print ('Server port 80 not connect!')
    global timer
    timer = threading.Timer(5.5, fun_timer)
    timer.start()
timer = threading.Timer(1, fun_timer)
timer.start()
#sk.close()

# try:
#   sk.connect(('106.14.18.151',12306))
#   print ('Server port 80 OK!')
# except Exception:
#   my_friend = bot.friends().search('爱上百合花')[0]
#   my_friend.send('Server port 12306 not connect!');
#   print ('Server port 80 not connect!')
# sk.close()



# timer = threading.Timer(1, fun_timer)
# timer.start()