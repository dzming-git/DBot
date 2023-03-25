# service.py
from my_example.app import func_dict, KEYWORD
from dbot import DBot

if __name__ == '__main__': 
    dbot = DBot()
    dbot.set_authority_config('my_example/conf/authority/authority.yaml')
    dbot.set_route_info_config('my_example/conf/route_info/route_info.yaml')
    dbot.set_consul_info_config('my_example/conf/consul_info/consul_info.yaml')
    dbot.set_keyword(KEYWORD)
    dbot.set_func_dict(func_dict)
    dbot.start()