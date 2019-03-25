# -*- coding: utf-8 -*-

import re
string1 = 'XXX高考时间是2018年6月7日'
string2 = 'XXX高考时间是2018/6/7'
string3 = 'XXX高考时间是2018-6-7'
string4 = 'XXX高考时间是2018-06-07'
string5 = 'XXX高考时间是2018-06'
string6 = 'XXX高考时间是2018年6月'

# regex_str = '.*高考时间是(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}(日|$)|[月/-]$|$))'
regex_str = '.*高考时间是(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}(日|$)|[月/-]|$))'

match_obj = re.match(regex_str, string6)
if match_obj:
    print(match_obj.group(1))


# regex_str = '.*高考时间是(\d{4}[年/-]\d{1,2}([月/-]|$)(\d{1,2}(日|$)|$))'
