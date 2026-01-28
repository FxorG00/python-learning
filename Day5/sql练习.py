from pymysql import  Connection
# Connection 是个类
# 构建连接对象
conn=Connection(
    host="localhost",
    port=3306,
    user='root',
    password='me20070513',
    autocommit=True
)
cursor=conn.cursor()
conn.select_db('py_sql')
# cursor.execute("create table orders(order_date date,order_id varchar(255),money int,province varchar(10))")
f=open('2011年1月销售数据.txt','r',encoding='UTF-8')
for line in f:
    nw="insert into orders values("
    nw_line=line.split(',')
    nw+=f"'{nw_line[0]}','{nw_line[1]}',{nw_line[2]},'{nw_line[3][:-1]}'"
    nw+=')'
    cursor.execute(nw)


