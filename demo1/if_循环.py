# 默认输入为字符串 需要int()方法转
age = int(input('请输入'))
if age >= 20:
  age -= 2
  print(age)
elif age == 18:
  print(age)
else:
  print(age)

indexList = [1,2,3,4,5]
total = 0
for index in indexList:
  total+=index
print(total)

n = len(indexList);
total = 0
while n > 0:
  n-=1
  if indexList[n] == 4:
    continue
  if total >= 10:
    break
  total+=indexList[n]

print(total)