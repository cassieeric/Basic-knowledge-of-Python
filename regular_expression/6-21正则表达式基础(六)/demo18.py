# -*- coding: utf-8 -*-

import re
string = 'xxx出生于2004年'

regex_str = '.*?(\d+)年'

match_obj = re.match(regex_str, string)
if match_obj:
    print(match_obj.group(1))
