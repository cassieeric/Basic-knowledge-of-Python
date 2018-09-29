# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import re

string = 'pcccpcccccccppppeng123'

regex_str = '.*?(p.*p).*'

match_obj = re.match(regex_str, string)
if match_obj:
    print(match_obj.group(1))


