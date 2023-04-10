import time
import socket
from dzmicro import singleton_server_manager, request_listen, send_message

def help(uuid: str, task):
    server_unique_info = singleton_server_manager.get_server_unique_info(uuid)
    authority = server_unique_info.authority
    source_id = task.get('source_id', None)
    gid, qid = source_id
    permission_level = authority.get_permission_level(source_id)
    permission = authority.get_permission_by_level(permission_level)
    if gid:
        message = f'[CQ:at,qq={qid}]\n'
    message = f'关键词 {KEYWORD}\n当前权限 {permission}\n可调用指令如下\n'
    for command in list(func_dict.keys()):
        if authority.check_command_permission(command, source_id):
            message += f'  - {command}\n'
    send_message(uuid, message.strip(), source_id)

def countdown(uuid: str, task):
    source_id = task.get('source_id', None)
    args = task.get('args', [])
    if not args:
        send_message(uuid, '缺少参数', source_id)
    else:
        time_countdown = int(args[0])
        while time_countdown > 0:
            send_message(uuid, f'倒计时 {time_countdown}', source_id)
            time_countdown -= 1
            time.sleep(1)
        send_message(uuid, '倒计时 结束', source_id)

def get_ip(uuid: str, task):
    source_id = task.get('source_id', None)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    send_message(uuid, ip_address, source_id)

def auto_echo(uuid: str, task):
    source_id = task.get('source_id', None)
    args = task.get('args', [])
    request_command = '自动复读'
    command = '复读'
    if not args or args[0] == '开始':        
        request_listen(uuid, request_command, command, source_id, True)
        send_message(uuid, '自动复读开始', source_id)
    elif args[0] == '停止':
        request_listen(uuid, request_command, command, source_id, False)
        send_message(uuid, '自动复读停止', source_id)

def echo(uuid: str, task):
    source_id = task.get('source_id', None)
    args = task.get('args', [])
    if args:
        send_message(uuid, args[0], source_id)

KEYWORD = '#测试'
func_dict = {
    '帮助':{
        'func': help,
        'permission': 'USER'
        },
    '倒计时': {
        'func': countdown,
        'permission': 'USER'
        },
    'IP':{
        'func': get_ip,
        'permission': 'USER'
        },
    '自动复读': {
        'func': auto_echo,
        'permission': 'ADMIN'
        },
    '复读': {
        'func': echo,
        'permission': 'INTERNAL'
        },
    }