from kazoo.client import KazooClient
import time
 
import logging
logging.basicConfig()
 
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()
 
@zk.DataWatch('/hosts')
def my_func(data, stat):
    if data:
        data = data.decode().replace(";","\n")
        print("Data is %s" % data)
        print("Version is %s\n" % stat.version)
    else :
        print("data is not available")
 
while True:
    time.sleep(10)

    print("next\n")
 
zk.stop()
