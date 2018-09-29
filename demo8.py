# -*- coding: utf-8 -*-

import re
string = 'ecpeng123'

regex_str = '([abcd]cpeng123)'

match_obj = re.match(regex_str, string)
if match_obj:
    print(match_obj.group(1))
