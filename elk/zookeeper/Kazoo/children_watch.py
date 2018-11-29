from kazoo.client import KazooClient
import time
 
import logging
logging.basicConfig()


map_1 = "127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4"
map_2 = "::1         localhost localhost.localdomain localhost6 localhost6.localdomain6"
 
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()
 
#@zk.DataWatch('/hosts')
url = "/hosts/"
filename = '/tmp/hosts'

f = open(filename,'w')
f.write(map_1 + '\n' + map_2 + '\n')
f.close()
@zk.ChildrenWatch(url)
def my_func(children):
    if children:
        f = open(filename,'a')
        for son in children:
            hosts = zk.get(url + son)[0].decode() + " " + son
            print("Children is %s" % son)
            print("Data is %s\n" % zk.get(url + son)[0].decode())
            f.write(hosts + '\n')
        f.close()
    else :
        print("data is not available")
 
while True:
    time.sleep(10)
 
zk.stop()
