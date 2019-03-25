# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import re

string = 'dcpeng1234'

regex_str = '^d.*'

match_obj = re.match(regex_str, string)
if match_obj:
    print('Yes')

