import re

info = """


idea [可以破解了] 时间是2020年2月12日，2020-02-12,"""
# print(info)

info2="""idea [可以破解了] 时间是2020年2月12日，2020-02-12,"""
# print(info)


res = re.match(r".*时间.*?(\d{4})", info, re.DOTALL)
# res = re.search("idea \[.*\]",info,re.DOTALL)
# res = re.search("idea \[.*\]",info2)


print(res.group(1))
