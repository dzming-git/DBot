from dzmicro import DzMicro
from dbot.dbot_server import creat_server
import time

class DBot(DzMicro):
    def __init__(self):
        super().__init__()
        self._dbot_server = None
    
    def start(self):
        if self.start_server():
            if self.is_platform():
                self._dbot_server = creat_server(self.handle)
                self._dbot_server.serve_forever()
        time.sleep(100)
