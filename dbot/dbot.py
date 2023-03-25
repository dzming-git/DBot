from dzmicro import DzMicro
from dbot.dbot_server import ServerCreator
from dbot.dbot_sender import send_message_to_cqhttp
from dzmicro.app.message_handler.message_handler import MessageHandlerThread
import time
from typing import Callable, List

class DBot(DzMicro):
    def __init__(self):
        super().__init__()
        self._dbot_server = None
        message_handler_thread = MessageHandlerThread()
        self.message_handler: Callable[[str, List], None] = message_handler_thread.message_handler
        self.set_send_message_to_source(send_message_to_cqhttp)
    
    def start(self):
        server_crator = ServerCreator()
        if self.start_server():
            if self.is_platform():
                server_crator.set_message_handler(self.message_handler)
                self._dbot_server = server_crator.creat_server()
                self._dbot_server.serve_forever()
        time.sleep(100)
    
