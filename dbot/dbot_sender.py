from typing import List
import requests
from dbot.urlencoding_message import urlencoding_message


def send_message_to_cqhttp(message: str, source_id: List, warn: bool = False):
    gid, qid = source_id
    urlencoded_message = urlencoding_message(message)
    if gid is None:
        requests.get(f'http://127.0.0.1:5700/send_private_msg?user_id={qid}&message={urlencoded_message}')
    else:   
        requests.get(f'http://127.0.0.1:5700/send_group_msg?group_id={gid}&message={urlencoded_message}')