f=open('2011年1月销售数据.txt','r',encoding='UTF-8')
for line in f:
    print(line.split(','))