import time, json, threading

class VolumeThread(threading.Thread):
    def __init__(self, vol):
        super(VolumeThread, self).__init__()
        self.stoprequest = threading.Event()
        self.websocket = None
        self.volume = vol
        self.last = -1

    def run(self):
        while not self.stoprequest.isSet():
            level = self.volume.level()

            if level != self.last and self.websocket:
                msg = json.dumps({'level': level})
                self.websocket.send(msg)
                self.last = level

            time.sleep(0.1)

    def join(self, timeout=None):
        self.stoprequest.set()
        super(VolumeThread, self).join(timeout)

