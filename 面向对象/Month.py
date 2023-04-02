from enum import Enum,unique

month = Enum('month', (
'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',
'Dec'))

# 枚举
@unique
class Weekday(Enum):
  Sun = 0 # Sun的value被设定为0
  Mon = 1
  Tue = 2
  Wed = 3
  Thu = 4
  Fri = 5
  Sat = 6