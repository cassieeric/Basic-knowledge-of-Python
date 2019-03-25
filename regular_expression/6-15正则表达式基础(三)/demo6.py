# -*- coding: utf-8 -*-

import re
string = 'dcpeng123'

regex_str = '[abcd]'

match_obj = re.match(regex_str, string)
if match_obj:
    print(match_obj.group(1))
