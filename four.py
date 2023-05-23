height=float(input("请输入身高(m):"))
weight=float(input("请输入体重(kg):"))
bim = weight /height**2
if bim<18.5:
    print("BIM指数为："+str(bmi))
    print("体重过轻")
elif bim>=24.and






x=input("请输入您的体重")
x=int(x)
if x<18.5:
elif 18.5<x<24.9:
    print("您体重正常")
elif 24.9<x<29.9:
    print("您体重过重")
elif x>29.9:
    print("肥胖")
