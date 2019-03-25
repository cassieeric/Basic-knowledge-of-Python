# -*- coding: utf-8 -*-

import re
string = 'dccpeng123'

regex_str = '((dcpeng|dccpeng)123)'

match_obj = re.match(regex_str, string)
if match_obj:
    print(match_obj.group(2))
