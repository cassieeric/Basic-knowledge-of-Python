# -*- coding: utf-8 -*-

import re
string = 'xxx graduates from 上海交通大学'

regex_str = '.*?([\u4E00-\u9FA5]+大学)'

match_obj = re.match(regex_str, string)
if match_obj:
    print(match_obj.group(1))
