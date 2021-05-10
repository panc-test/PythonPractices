"""
datetime - time 时间模块升级版本
1.date类
2.time类
3.datetime类

"""
import datetime

# # date 日期类，包含年、月、日。精确度到天
# print("***这是类方法***")
# print(datetime.date)
# print(datetime.date.today())
# print(datetime.date.fromtimestamp(0))   # 参数是时间戳
#
# print("***这是实例方法***")
# t = datetime.date(2021,5,10)
# print(t)
# print(t.today())
# print(t.ctime())    # 返回一个ctime格式的日期字符串
# print(t.isoformat())    # 返回一个iso格式的日期字符串
# print(t.strftime("%Y-%m-%d %a"))    # 返回一个自定义格式的日期字符串




# # time 时间类，包含时、分、秒、微秒。精确到微秒，而且可以具有时区(tzinfo)属性。
# print("***这是类方法***")
# print(datetime.time)
#
# print("***这是实例方法***")
# t = datetime.time(17,47,50)
# print(t.hour)
# print(t.isoformat())    # 返回一个iso格式的时间字符串
# print(t.strftime('%H:%M:%S %p'))    # 返回一个自定义格式的时间字符串




# # datetime 日期时间类，包含date和time的所有信息
# print("***这是类方法***")
# print(datetime.datetime)
# print(datetime.datetime.today())
# print(datetime.datetime.now())      # 返回当前本地时间
# print(datetime.datetime.utcnow())   # 返回当前utc时间
# print(datetime.datetime.fromtimestamp(0))       # 根据时间戳返回本地时间
# print(datetime.datetime.utcfromtimestamp(0))    #根据时间戳返回UTC时间
#
# print("***这是实例方法***")
# t = datetime.datetime(year=2020,month=5,day=10,hour=18,minute=32,second=30)     # 实例化对象，年月日必填
# print(t)
# print(t.date())     # 返回date对象
# print(t.time())     # 返回time对象
# print(t.ctime())    # 返回一个ctime格式的日期时间字符串
# print(t.isoformat())    # 返回一个iso格式的日期时间字符串
# print(t.strftime("%Y-%m-%d"))


