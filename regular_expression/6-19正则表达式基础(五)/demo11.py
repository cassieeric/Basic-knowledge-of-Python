# -*- coding: utf-8 -*-

import re
string = '加 油'

regex_str = '(加\s油)'

match_obj = re.match(regex_str, string)
if match_obj:
    print(match_obj.group(1))
