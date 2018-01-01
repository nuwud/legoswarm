#!/usr/bin/env python3

import socket
import logging
import sys
import time
from threading import Thread
try:
    import cPickle as pickle
except:
    import pickle

class CameraUDP(Thread):
    def __init__(self, port=50008):
        ### Initialize ###
        self.port = port
        self.robot_broadcast_data = {'markers': {}, 'balls': {}, 'settings': {}}
        self.running = True

        ### Create a socket ###
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(('', self.port))
        Thread.__init__(self)
        print("Started thread")

    def stop(self):
        print("Stopping thread")
        self.runnning = False

    def get_data(self):
        return self.robot_broadcast_data

    ### Get robot positions from server ###
    def run(self):
        """
        Thread that writes UDP data into a global: robot_broadcast_data

        Usage:
        get_positions_thread = Thread(target=get_camera_data)
        get_positions_thread.start()

        to clean up:
        running=False
        :return:
        """

        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(('', self.port))

        while self.running:
            try:
                data, server = self.s.recvfrom(2048)
                self.robot_broadcast_data = pickle.loads(data)
            except:
                e = sys.exc_info()[0]
                logging.warning(e)
                raise

        self.s.close()

    


if __name__ == '__main__':
    camera_thread = CameraUDP()
    camera_thread.start()
    for t in range(100):
        time.sleep(0.5)
        try:
            # Get robot positions from server
            print(camera_thread.get_data())
        except:
            # Time to panic, log some errors and kill others threads.
            camera_thread.stop()
            raise