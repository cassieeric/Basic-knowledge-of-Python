# -*- coding: utf-8 -*-

import re
string = 'pcccpcccccccphhpeng123'

regex_str = '.*(p.+p).*'

match_obj = re.match(regex_str, string)
if match_obj:
    print(match_obj.group(1))
