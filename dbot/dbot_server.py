from flask import Flask, request
from werkzeug.serving import make_server
from typing import Callable, List

class ServerCreator:
    _message_handler: Callable[[str, List], None] = None

    @classmethod
    def set_message_handler(cls, message_handler: Callable[[str, List], None]):
        cls._message_handler = message_handler

    @classmethod
    def creat_server(cls):
        app = Flask(__name__)
        @app.route('/', methods=["POST"])
        def post_data():
            '''
            将信息源的信息转发至服务程序
            '''
            # 获取消息体
            data = request.get_json()
            print(data)
            # 获取source_id
            qid = data.get('sender', {}).get('user_id')
            gid = data.get('group_id')
            source_id = [gid, qid]
            # 获取原始消息内容
            message = data.get('raw_message')
            cls._message_handler(message, source_id)
            # 返回响应
            return 'OK'
        server = make_server(host='127.0.0.1', port=5701, app=app)
        return server
