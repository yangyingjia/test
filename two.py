import datetime
sex=["女","男"]
id=input("请输入你的身份证号：")
year=int(id[6:10])
month=int(id[10:12])
day=int(id[12:14])
#数据处理和输出
print("你的出生{}年{}月{}日".format(year,month,day))
age=int(datetime.datetime.now().year-year)
print("你{}岁".format(age))
mysex=int(id[16])
sex2=(sex[mysex%2])
print("你的性别为{}".format(sex2))
