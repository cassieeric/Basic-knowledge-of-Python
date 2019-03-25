# -*- coding: utf-8 -*-

import re
string = '16042682515'

regex_str = '(1[34578][0-9]{9})'

match_obj = re.match(regex_str, string)
if match_obj:
    print(match_obj.group(1))
