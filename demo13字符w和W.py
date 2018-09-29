# -*- coding: utf-8 -*-

import re
string = '加a油'

regex_str = '(加[A-Za-z0-9_]油)'

match_obj = re.match(regex_str, string)
if match_obj:
    print(match_obj.group(1))
