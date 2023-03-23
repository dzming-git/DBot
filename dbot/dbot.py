from dzmicro import DzMicro
from dbot.dbot_server import creat_server
from dbot.dbot_sender import send_message_to_cqhttp
import time

class DBot(DzMicro):
    def __init__(self):
        super().__init__()
        self._dbot_server = None
        self.set_send_message_to_source(send_message_to_cqhttp)
    
    def start(self):
        if self.start_server():
            if self.is_platform():
                self._dbot_server = creat_server(handle_func=self.handle)
                self._dbot_server.serve_forever()
        time.sleep(100)
    
