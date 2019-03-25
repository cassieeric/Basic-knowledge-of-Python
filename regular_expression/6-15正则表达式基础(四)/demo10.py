# -*- coding: utf-8 -*-

import re
string = '18ddddddddd'

regex_str = '(1[34578][^1]{9})'

match_obj = re.match(regex_str, string)
if match_obj:
    print(match_obj.group(1))
