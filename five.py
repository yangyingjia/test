import a
list = [1,0,0,0]
list1 = [0,0,0,0]
sum1 = 0
x = int(input ("请输入月份："))
for i in range(x+1):
    if i<3:
        sum1 = 1
    else:
        list1[2] = list[3]
        list1[1] = list[2]
        list1[0] = list[1] + list[0]
        list1[3] = list[0]
        list = a.a(list1)
        print("list:",list1)
        sum1 = sum(list1)
print("兔子的总数为:",sum1)


