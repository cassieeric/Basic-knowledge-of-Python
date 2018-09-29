# -*- coding: utf-8 -*-

import re
string = '加加油油'

regex_str = '(加\S+油)'

match_obj = re.match(regex_str, string)
if match_obj:
    print(match_obj.group(1))
