# Introduction
This folder is designed to store regular expression basic knowledege.

# 正则表达式初识，关于特殊字符的介绍 

1、“^”代表的意思是限定以某个字符开头，具体用法可以参考这篇文章：Python正则表达式初识（一）。 

2、“*”代表的意思是限定前面的字符出现任意多次，这个任意多次包括0次，即次数大于等于0。具体用法可以参考这篇文章：Python正则表达式初识（一）。 

3、“.”代表的意思是任意字符，其范围非常广，包含了所有的字符。具体用法可以参考这篇文章：Python正则表达式初识（一）。 

4、“$”代表的意思是限定以某个字符结尾。具体用法可以参考这篇文章：Python正则表达式初识（二）。 
5、“?”代表的意思是非贪婪模式。具体用法可以参考这篇文章：Python正则表达式初识（二）。 
6、“+”代表的意思是限定前面的字符出现任意多次，这个任意多次不包括0次，至少出现1次，即次数大于等于1。具体用法可以参考这篇文章：Python正则表达式初识（三）。 
7、“{2}”、“{2,}”、“{2,5}”三种表达方式，限定前面的字符出现的次数。“{2}”代表前面的字符出现两次；“{2,}” 代表前面的字符出现两次以上；“{2,5}” 代表前面的字符出现两次到5次之间。具体用法可以参考这篇文章：Python正则表达式初识（四）。 
8、“|”代表的意思是该竖线两边的值只需要匹配上其中一个即可，就可以满足要求，相当于逻辑运算关系中的“或”。具体用法可以参考这篇文章：Python正则表达式初识（五）。 
9、“[]”、“[A-Za-z0-9]”、“[^]”三种表达方式。“[]”表示中括号中出现的任意一个字符；“[A-Za-z0-9]”表示取值区间；“[^]”代表的意思是非、取反的意思。具体用法可以参考这篇文章：Python正则表达式初识（六）。 
10、“\s”的意思是代表空格，“\S”的意思是代表非空格。具体用法可以参考这篇文章：Python正则表达式初识（七）。 
11、“\w”的意思是代表26个大小写字母、0-9共10个数字以及下划线，即表达式[A-Za-z0-9_]所代表的内容；“\W”的意思和“\w”相反，代表的是除了表达式[A-Za-z0-9_]代表的内容之外的其他所有字符。具体用法可以参考这篇文章：Python正则表达式初识（八）。 
12、“[\u4E00-\u9FA5]” 这个区间代表的意思是汉字。具体用法可以参考这篇文章：Python正则表达式初识（九）。 
13、“()”是用于提取子字符串用的，在正则表达式的每篇文章中都有提及。 
14、“\d”的意思是代表数字类型。 
关于具体的正则表达式用法，可以参考我的个人博客：https://www.zhihu.com/people/peng-dong-cheng-38/posts

【2019年5月24日更新】
上传了微信群张帆整理的正则表达式速记.txt文档，花几分钟学习一下，就会懂很多，希望对大家对于正则表达式的理解有帮助。