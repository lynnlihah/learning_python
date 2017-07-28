#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# datetime - 处理日期和时间的标准库
from datetime import datetime # datetime 是一个模块， import 的datetime是一个类
now = datetime.now() # 当前时间
print(now)
print(type(now)) # <class 'datetime.datetime'>

dt = datetime(1988,2,16,12,20)# 获得指定时间
print(dt) # 1988-02-16 12:20:00

# datetime 和 timestamp互转

# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，
# 记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
# 可以认为 timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
# 对应的北京时间是  timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
# 可见timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全
# 确定的，这就是为什么计算机存储的当前时间是以timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都
# 是完全相同的（假定时间已校准）。

print(dt.timestamp()) # 571983600.0 - 把datetime转换为 timestamp
# 注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
t = 571983600.0
print(datetime.fromtimestamp(t)) # 1988-02-16 12:20:00 timestamp转datetime - 本地时间
# timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换。
# 实际就是 1988-02-16 12:20:00 UTC+8:00 而此事格林威治标准时间与北京时间相差了8小时，
# 所以UTC+0：00时区的时间应该是 1988-02-16 08:20:00 UTC+0:00
print(datetime.utcfromtimestamp(t)) #　1988-02-16 04:20:00 UTC标准时


# datetime 和 str 互转 - 用户处理用户直接输入的字符串
cday = datetime.strptime('1988-02-16 18:19:59', '%Y-%m-%d %H:%M:%S') # str 转 datetime
print(cday) # 1988-02-16 18:19:59

print(now.strftime('%a, %b %d %H:%M')) # datetime 转 str - Fri, Jul 28 09:28

# datetime 加减
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过
# 需要导入timedelta这个类
from datetime import timedelta
print(now) #　2017-07-28 09:31:45.991401
print(now + timedelta(hours=10)) # 2017-07-28 19:31:45.991401
print(now - timedelta(days=1)) # 2017-07-27 09:31:45.991401
print(now + timedelta(days=2, hours=12)) # 2017-07-30 21:31:45.991401

# 本地时间转换为UTC时间
# 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
print(now) # 2017-07-28 09:54:59.751401
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print(dt) # 2017-07-28 09:54:59.751401+08:00
# 如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。

# 时区转换
# 可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc) # 拿到UTC时间，并强制设置时区为UTC+0:00:
print(utc_dt) # 2017-07-28 03:30:06.594401+00:00
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8))) # astimezone()将转换时区为北京时间:
print(bj_dt) # 2017-07-28 11:30:06.594401+08:00
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9))) # astimezone()将转换时区为东京时间:
print(tokyo_dt) # 2017-07-28 12:30:06.594401+09:00
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9))) #  astimezone()将bj_dt转换时区为东京时间:
print(tokyo_dt2) # 2017-07-28 12:30:06.594401+09:00



