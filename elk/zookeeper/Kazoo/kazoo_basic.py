#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: kazoo_basic.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com 
#  Created Time: 2018-09-10 16:54:44
#########################################################################

#!/usr/bin/py3

import time

from kazoo.client import KazooClient

from kazoo.client import KazooState

 

def main():

    zk=KazooClient(hosts='127.0.0.1:2181')

    zk.start()

    

    @zk.add_listener

    def my_listener(state):

        if state == KazooState.LOST:

            print("LOST")

        elif state == KazooState.SUSPENDED:

            print("SUSPENDED")

        else:

            print("Connected")

    #Creating Nodes

    # Ensure a path, create if necessary
    if zk.exists("/my"):
        zk.delete("/my", recursive=True)

    zk.ensure_path("/my/favorite")

    # Create a node with data

    zk.create("/my/favorite/node", b"/my/favorite/node")

    zk.create("/my/favorite/node/a", b"A")

    #Reading Data

    # Determine if a node exists

    if zk.exists("/my/favorite"):

        print("/my/favorite is existed")

    @zk.ChildrenWatch("/my/favorite/node")

    def watch_children(children):

        print("Children are now: %s" % children)

    # Above function called immediately, and from then on

    @zk.DataWatch("/my/favorite/node")

    def watch_node(data, stat):

        print("Version: %s, data: %s" % (stat.version, data.decode()))

    # List the children

    children = zk.get_children("/my/favorite/node")

    print("There are %s children with names %s" % (len(children), children))

    #Updating Data

    zk.set("/my/favorite", b"some data")

    #Deleting Nodes

    zk.delete("/my/favorite/node/a")


    transaction = zk.transaction()

    transaction.check('/my/favorite/node', version=-1)

    transaction.create('/my/favorite/node/b', b"B")

    results = transaction.commit()

    print ("Transaction results is %s" % results)

    zk.delete("/my/favorite/node/b")

    zk.delete("/my", recursive=True)

    time.sleep(2)

    zk.stop()

 

if __name__ == "__main__":

    try:

        main()

    except Exception as ex:

        print("Ocurred Exception: %s" % str(ex))

        quit()
