# -*- coding: utf-8 -*-

import re
string = 'dccccpapaaphhhhpeng123'

regex_str = '.*(p.{3,5}p).*'

match_obj = re.match(regex_str, string)
if match_obj:
    print(match_obj.group(1))
